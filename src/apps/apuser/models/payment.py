from django.db import models
from django.db.models.query import QuerySet
from django.utils.translation import ugettext_lazy as _
from catalog.models.currency import Currency


class BillQueryset(QuerySet):
    def by_user(self, user):
        return self.filter(user=user)


class BillManager(models.Manager):
    def make(self, user):
        return True


class Bill(models.Model):
    user = models.ForeignKey('apuser.AlterPriceUser',
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
    user = models.ForeignKey('apuser.AlterPriceUser',
                             verbose_name=_('Пользователь'))
    amount = models.IntegerField(default=0,
                                 verbose_name=_('Сумма'))

    currency = models.ForeignKey(Currency,
                                 verbose_name=_('Валюта'))

    objects = PaymentManager.from_queryset(PaymentQueryset)()

    def is_payment(self):
        return True if self.payment_detail is self.PAYMENT else False

    def is_recovery(self):
        return True if self.payment_detail is self.RECOVER else False

    class Meta:
        verbose_name = _('Оплата')
        verbose_name_plural = _('Оплаты')


class InvoiceRequest(models.Model):
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
