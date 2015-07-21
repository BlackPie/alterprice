from django.db import models
from django.db.models.query import QuerySet
from django.utils.translation import ugettext_lazy as _
from catalog.models.currency import Currency


class Payment(models.Model):
    BILL = 0
    ONLINE = 1

    TYPE_CHOICES = (
        (BILL, _('Банковский счет')),
        (ONLINE, _('Онлайн оплата')),
    )

    PAYMENT = 0
    RECOVER = 1

    DETAIL_CHOICES = (
        (PAYMENT, _('Платеж')),
        (RECOVER, _('Возврат средств'))
    )
    payment_type = models.PositiveSmallIntegerField(verbose_name=_('Тип платежа'),
                                                    default=BILL,
                                                    choices=TYPE_CHOICES)

    payment_detail = models.PositiveSmallIntegerField(verbose_name=_(u'Основание платежа'),
                                                      default=PAYMENT,
                                                      choices=DETAIL_CHOICES)
    created = models.DateTimeField(auto_now_add=True,
                                   editable=False,
                                   verbose_name=_(u'Дата создания'))
    client = models.ForeignKey('apuser.ClientProfile',
                             verbose_name=_('Клиент'))
    amount = models.IntegerField(default=0,
                                 verbose_name=_('Сумма'))

    currency = models.ForeignKey(Currency,
                                 verbose_name=_('Валюта'), blank=True, null=True)
    robokassa_success = models.BooleanField(default=False)

    def is_payment(self):
        return True if self.payment_detail is self.PAYMENT else False

    def is_recovery(self):
        return True if self.payment_detail is self.RECOVER else False

    class Meta:
        verbose_name = _('Оплата')
        verbose_name_plural = _('Оплаты')


class InvoiceRequest(models.Model):
    created = models.DateTimeField(auto_now=True)
    client = models.ForeignKey('apuser.ClientProfile', verbose_name=_('Клиент'))
    invoice_file = models.FileField(blank=True, null=True, verbose_name=_('Файл счета'))
    company_name = models.CharField(verbose_name=_('Компания'), max_length=255)
    inn = models.CharField(verbose_name=_('ИНН'), max_length=255)
    kpp = models.CharField(verbose_name=_('КПП'), max_length=255)
    bik = models.CharField(verbose_name=_('БИК'), max_length=255)
    rs = models.CharField(verbose_name=_('Рассчетный счет'), max_length=255)
    ks = models.CharField(verbose_name=_('Корреспондетский счет'), max_length=255)
    bank_name = models.CharField(verbose_name=_('Название банка'), max_length=255)
    fio = models.CharField(verbose_name=_('ФИО контактного лица'), max_length=255)
    phone = models.CharField(verbose_name=_('Телефон контактного лица'), max_length=255)
    legal_address = models.CharField(verbose_name=_('Юридический адрес'), max_length=255)
    post_address = models.CharField(verbose_name=_('Почтовый адрес'), max_length=255)
