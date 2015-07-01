from django.db import models
from django.utils.translation import ugettext_lazy as _
from .apuser import AlterPriceUser as User
from .payment import Payment
from .click import Click
from shop.models import Shop


class MakeException(Exception):
    ""


class BalanceManager(models.Manager):
    def make(self, user):
        if not isinstance(user, User):
            raise MakeException('invalid user object')
        obj = self.model(user=user)
        obj.save()
        return obj


class Balance(models.Model):
    user = models.OneToOneField(User,
                                verbose_name=_('Пользователь'))
    value = models.IntegerField(default=0,
                                verbose_name=_('Значние'))

    def __str__(self):
        return self.user

    def __unicode__(self):
        return self.user

    objects = BalanceManager()

    class Meta:
        verbose_name = _('Баланс')
        verbose_name_plural = _('Баланс')


class BalanceHistoryManager(models.Manager):
    def make(self, balance, value, previous_state, new_state, reason,
             payment=None, click=None):
        obj = self.model()
        obj.balance = balance
        obj.value = value
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
            Shop.objects.turn_off_debtor(balance.user)
        return obj

    def increase(self, balance, value, payment):
        return self.make(
            balance=balance,
            reason=self.model.REPLISHMENT,
            payment=payment,
            previous_state=balance.value,
            value=value,
            new_state=balance.value + value)

    def decrease(self, balance, value, click):
        new_state = balance.value - value
        obj = self.make(
            balance=balance,
            reason=self.model.CLICK,
            click=click,
            previous_state=balance.value,
            value=value,
            new_state=new_state)
        return obj

    def recover(self, balance, value, payment):
        return self.make(
            balance=balance,
            reason=self.model.RECOVERY,
            payment=payment,
            previous_state=balance.value,
            value=value,
            new_state=balance.value + value)


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
        return self.balance

    def __unicode__(self):
        return self.balance

    class Meta:
        verbose_name = _('Изменение баланса')
        verbose_name_plural = _('Изменения баланса')
