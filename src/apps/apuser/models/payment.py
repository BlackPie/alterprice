from django.db import models
from django.utils.translation import ugettext_lazy as _
from .apuser import AlterPriceUser as User
from catalog.models import Currency


class Balance(models.Model):
    user = models.OneToOneField(User,
                                verbose_name=_('Пользователь'))
    value = models.IntegerField(default=0,
                                verbose_name=_('Значние'))

    class Meta:
        verbose_name = _('Баланс')
        verbose_name_plural = _('Баланс')


class Bill(models.Model):
    user = models.ForeignKey(User,
                             verbose_name=_('Пользователь'))
    created = models.DateTimeField(auto_now_add=True,
                                   editable=False,
                                   verbose_name=_(u'Дата создания'))
    amount = models.IntegerField(default=0,
                                 verbose_name=_('Сумма'))

    class Meta:
        verbose_name = _('Счет')
        verbose_name_plural = _('Счета')


class Payment(models.Model):
    BILL = 0
    ONLINE = 1

    PAYMENT_CHOICES = (
        (BILL, _('Банковыский счет')),
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

    class Meta:
        verbose_name = _('Оплата')
        verbose_name_plural = _('Оплаты')
