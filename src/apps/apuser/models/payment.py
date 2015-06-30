from django.db import models
from django.db.models.query import QuerySet
from django.utils.translation import ugettext_lazy as _
from .apuser import AlterPriceUser as User
from catalog.models import Currency


class BillQueryset(QuerySet):
    def by_user(self, user):
        return self.filter(user=user)


class BillManager(models.Manager):
    def make(self, user):
        return True


class Bill(models.Model):
    user = models.ForeignKey(User,
                             verbose_name=_('Пользователь'))
    created = models.DateTimeField(auto_now_add=True,
                                   editable=False,
                                   verbose_name=_(u'Дата создания'))
    amount = models.IntegerField(default=0,
                                 verbose_name=_('Сумма'))

    objects = BillManager.from_queryset(BillQueryset)()

    class Meta:
        verbose_name = _('Счет')
        verbose_name_plural = _('Счета')


class PaymentQueryset(QuerySet):
    def by_user(self, user):
        return self.filter(user=user).select_related('currency')


class PaymentManager(models.Manager):
    def make(self):
        return True


class Payment(models.Model):
    BILL = 0
    ONLINE = 1

    PAYMENT_CHOICES = (
        (BILL, _('Банковский счет')),
        (ONLINE, _('Онлайн оплата')),
    )
    payment_type = models.PositiveSmallIntegerField(verbose_name=_(u'Тип оплаты'),
                                                    default=BILL,
                                                    choices=PAYMENT_CHOICES)
    created = models.DateTimeField(auto_now_add=True,
                                   editable=False,
                                   verbose_name=_(u'Дата создания'))
    user = models.ForeignKey(User,
                             verbose_name=_('Пользователь'))
    amount = models.IntegerField(default=0,
                                 verbose_name=_('Сумма'))

    currency = models.ForeignKey(Currency,
                                 verbose_name=_('Валюта'))

    objects = PaymentManager.from_queryset(PaymentQueryset)()

    class Meta:
        verbose_name = _('Оплата')
        verbose_name_plural = _('Оплаты')
