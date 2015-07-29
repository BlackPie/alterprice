from datetime import datetime, timedelta
from django.db import models
from django.db.models import Sum
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from .apuser import AlterPriceUser as User
from apuser.models import ClientProfile
from django.db.models.signals import post_save
from apuser.models.payment import Payment
from apuser.models.profile import EmailDelivery
from .click import Click
from django.core.cache import cache
from shop.models.shop import Shop


class MakeException(Exception):
    ""


class BalanceManager(models.Manager):
    def make(self, client):
        if not isinstance(client, ClientProfile):
            raise MakeException('invalid client object')
        obj = self.model(client=client)
        obj.save()
        return obj


class Balance(models.Model):
    client = models.OneToOneField(ClientProfile,
                                verbose_name=_('Клиент'))
    value = models.IntegerField(default=0,
                                verbose_name=_('Значние'))

    def __unicode__(self):
        return str(self.client)

    def __str__(self):
        return str(self.client)

    objects = BalanceManager()

    class Meta:
        verbose_name = _('Баланс')
        verbose_name_plural = _('Баланс')

SPENT_LAST_DAY_PREFIX = 'spent_last_day'

@receiver(post_save, sender=Balance)
def balance_change_callback(sender, instance, **kwargs):
    active = bool(instance.value > 0)
    now = datetime.now()
    date = now.replace(second=0, microsecond=0, minute=0, hour=0)
    cache_key = '%s:%d:%d' % (SPENT_LAST_DAY_PREFIX, now.day, instance.client.id)
    money_sum = cache.get(cache_key)
    if not money_sum:
        money_sum = BalanceHistory.objects.filter(balance__client=instance.client,
                                  created__gte=date - timedelta(days=1),
                                  created__lt=date).aggregate(Sum('change_value'))
        money_sum = money_sum['change_value__sum']
        cache.set(cache_key, money_sum)
        cache.expire(cache_key, timeout=60*60*24)
    if money_sum and money_sum * 3 > instance.value and money_sum > 1000:
        EmailDelivery.objects.make(
            template='client/balance_limit.html',
            email=instance.client.user.email,
            context={'balance': instance.value},
        )
        if instance.client.operator:
            EmailDelivery.objects.make(
                template='client/balance_limit.html',
                email=instance.client.operator.user.email,
                context={'balance': instance.value, 'client': instance.client},
            )
        instance.client.limit_balance_email_send = True
    if money_sum is not None and money_sum <= 0:
        EmailDelivery.objects.make(
            template='client/balance_zero.html',
            email=instance.client.user.email,
            context={'balance': instance.value},
        )
        instance.client.zero_balance_email_send = True
    if (instance.client.is_active != active):
        # shops = Shop.objects.filter(user=instance.client.user)
        # status = Shop.ENABLED if active else Shop.DISABLED
        # shops.update(status=status)
        instance.client.is_active = active
    instance.client.save()


class BalanceHistoryManager(models.Manager):
    def make(self, balance, value, previous_state, new_state, reason,
             payment=None, click=None):
        obj = self.model()
        obj.balance = balance
        obj.change_value = value
        obj.previous_state = previous_state
        obj.new_state = new_state
        if payment:
            obj.payment = payment
        if click:
            obj.click = click
        obj.reason = reason
        obj.save()
        # Update balance
        balance.value = new_state
        balance.save()
        if new_state <= 0:
            # Turns off (status=Disabled) all shops of balance.user
            Shop.objects.turn_off_debtor(balance.client.user)
        return obj

    def increase(self, balance, payment):
        return self.make(
            balance=balance,
            reason=self.model.REPLISHMENT,
            payment=payment,
            previous_state=balance.value,
            value=payment.amount,
            new_state=balance.value + payment.amount)

    def decrease(self, balance, value, click):
        new_state = balance.value - value

        return self.make(
            balance=balance,
            reason=self.model.CLICK,
            click=click,
            previous_state=balance.value,
            value=value,
            new_state=new_state)

    def recover(self, balance, payment):
        return self.make(
            balance=balance,
            reason=self.model.RECOVERY,
            payment=payment,
            previous_state=balance.value,
            value=payment.amount,
            new_state=balance.value + payment.amount)


class BalanceHistory(models.Model):
    CLICK = 0
    REPLISHMENT = 1
    RECOVERY = 2

    REASON_CHOICES = (
        (CLICK, _('Клик')),
        (REPLISHMENT, _('Пополнение')),
        (RECOVERY, _('Восстановление')),
    )

    balance = models.ForeignKey(Balance,
                                verbose_name=_('Баланс'))
    created = models.DateTimeField(auto_now_add=True,
                                   editable=False,
                                   verbose_name=_(u'Дата создания'))
    previous_state = models.IntegerField(default=0,
                                         verbose_name=_('Предидущее состояние баланса'))
    change_value = models.IntegerField(default=0,
                                       verbose_name=_('Величина изменения'))
    new_state = models.IntegerField(default=0,
                                    verbose_name=_('Новое состояние'))
    reason = models.PositiveSmallIntegerField(verbose_name=_(u'Основание'),
                                              default=CLICK,
                                              choices=REASON_CHOICES)
    payment = models.ForeignKey(Payment,
                                default=None,
                                null=True,
                                blank=True,
                                verbose_name=_('Платеж'))
    click = models.ForeignKey(Click,
                              default=None,
                              null=True,
                              blank=True,
                              verbose_name=_('Клик'))

    objects = BalanceHistoryManager()

    def __str__(self):
        return str(self.balance.client)

    def __unicode__(self):
        return (self.balance.client)

    class Meta:
        verbose_name = _('Изменение баланса')
        verbose_name_plural = _('Изменения баланса')
