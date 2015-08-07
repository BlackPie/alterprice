from django.db import models
from django.core.validators import EMPTY_VALUES
from django.utils.translation import ugettext_lazy as _
# Project imports
from django_extensions.db.fields.json import JSONField
from .apuser import AlterPriceUser
from apuser.models.payment import InvoiceRequest
from django.db.models.signals import post_save, pre_save
from django.dispatch.dispatcher import receiver
from utils.helpers import generate_code
from utils.abstract_models import ApprovedModel, is_choice_of


class MakeException(Exception):
    ""


class Profile(models.Model):
    phone = models.CharField(max_length=100,
                             blank=True,
                             null=True,
                             default=None,
                             verbose_name=_(u'Телефон'))
    name = models.CharField(max_length=150,
                            null=True,
                            blank=True,
                            verbose_name=_(u'Имя'))
    last_name = models.CharField(max_length=150,
                                 null=True,
                                 blank=True,
                                 verbose_name=_(u'Фамилия'))

    class Meta:
        abstract = True


class AdminProfile(Profile):
    user = models.OneToOneField(AlterPriceUser,
                                related_name='admin_user',
                                verbose_name=_('Пользователь'))

    class Meta:
        verbose_name = _('Администратор')
        verbose_name_plural = _('Администраторы')


class OperatorProfile(Profile):
    user = models.OneToOneField(AlterPriceUser,
                                related_name='operator_user',
                                verbose_name=_('Пользователь'))
    code = models.CharField(max_length=5,
                            default=generate_code,
                            verbose_name=_('Код'))

    def __str__(self):
        return '%s  %s' % (self.last_name, self.name)

    def __unicode__(self):
        return '%s  %s' % (self.last_name, self.name)

    class Meta:
        verbose_name = _('Оператор')
        verbose_name_plural = _('Операторы')
        ordering = ('name',)


class ClientProfileManager(models.Manager):
    def make(self, user, operator=None, name=None, last_name=None,
             company=None, city=None, ownership_type=None):
        if not isinstance(user, AlterPriceUser):
            raise MakeException('invalid user obj')
        if operator not in EMPTY_VALUES:
            if not isinstance(operator, OperatorProfile):
                raise MakeException('invalid operator obj')
        if not (ownership_type, self.model.OWNERSHIP_CHOICES):
            ownership_type = self.model.ENTITY
        obj = self.model()
        obj.user = user
        obj.name = name
        if operator:
            obj.operator = operator.user
        obj.last_name = last_name
        obj.ownership_type = ownership_type
        obj.company = company
        obj.city = city
        obj.save()
        return obj


class ClientProfile(Profile):
    ENTITY = 0
    INDIVIDUAL = 1

    OWNERSHIP_CHOICES = (
        (ENTITY, _('Юридическое лицо')),
        (INDIVIDUAL, _('Физическое лицо')),
    )

    user = models.OneToOneField(AlterPriceUser,
                                related_name='client_profile',
                                verbose_name=_('Пользователь'))
    ownership_type = models.PositiveSmallIntegerField(verbose_name=_(u'Форма собственности'),
                                                      default=ENTITY,
                                                      choices=OWNERSHIP_CHOICES)
    city = models.CharField(max_length=255,
                            default=None,
                            blank=True,
                            null=True,
                            verbose_name=_('Город'))
    company = models.CharField(max_length=255,
                               default=None,
                               blank=True,
                               null=True,
                               verbose_name=_('Название компании'))
    operator = models.ForeignKey(AlterPriceUser,
                                 null=True,
                                 blank=True,
                                 default=None,
                                 related_name='operator',
                                 verbose_name=_('Оператор'))
    checked = models.BooleanField(default=False, verbose_name=_('Проверено'), help_text=_('Модератор проверил и одобрил'))
    is_active = models.BooleanField(default=False, verbose_name=_('Активен'), help_text=_('Неактивен если закончились деньги на балансе'))
    objects = ClientProfileManager()
    limit_balance_email_send = models.BooleanField(default=False)
    zero_balance_email_send = models.BooleanField(default=False)

    def __unicode__(self):
        return self.company or 'Client %d' % self.id

    def __str__(self):
        return self.company or 'Client %d' % self.id

    @property
    def invoices(self):
        return InvoiceRequest.objects.filter(client=self) \
            .exclude(invoice_file='')

    class Meta:
        verbose_name = _('Клиент')
        verbose_name_plural = _('Клиенты')


@receiver(pre_save, sender=ClientProfile)
def client_profile_change_pre_callback(sender, instance, **kwargs):
    instance._operator_id_old = instance.operator_id


@receiver(post_save, sender=ClientProfile)
def client_profile_change_callback(sender, instance, **kwargs):
    if instance._operator_id_old != instance.operator_id and instance.operator_id:
        EmailDelivery.objects.make(
            template='operator/client_set.html',
            email=instance.operator.user.email,
            context={'client': instance},
        )


class ClientPaymentInfo(models.Model):
    client = models.OneToOneField(ClientProfile,
                                  verbose_name=_('Клиент'))
    org_name = models.CharField(max_length=255,
                                verbose_name=_('Название организации'))
    inn = models.CharField(max_length=255,
                           verbose_name=_('ИНН'))
    kpp = models.CharField(max_length=255,
                           verbose_name=_('КПП'))
    bik = models.CharField(max_length=255,
                           verbose_name=_('БИК'))
    rs = models.CharField(max_length=255,
                          verbose_name=_('Р/С'))
    corp_bill = models.CharField(max_length=255,
                                 verbose_name=_('Кор. счет'))
    bank_name = models.CharField(max_length=255,
                                 verbose_name=_('Название банка'))
    contact_name = models.CharField(max_length=255,
                                    verbose_name=_('ФИО контактного лица'))
    contact_phone = models.CharField(max_length=255,
                                     verbose_name=_('Телефон контактного лица'))
    legal_address = models.CharField(max_length=255,
                                     verbose_name=_('Юридический адрес'))
    post_address = models.CharField(max_length=255,
                                    verbose_name=_('Почтовый адрес'))

    def __str__(self):
        return self.org_name

    def __unicode__(self):
        return self.org_name

    class Meta:
        verbose_name = _('Платежные данные клиента')
        verbose_name_plural = _('Платежные данные клиентов')

class EmailDeliveryManager(models.Manager):
    def make(self, template, email, context=None):
        if not email:
            raise Exception('Email cant be blank')
        return self.create(
            template=template,
            email=email,
            context=context,
        )

class EmailDelivery(models.Model):
    NEW = 0
    SUBMITTED = 1
    STATUS_CHOICES = (
        (NEW, _('Новое')),
        (SUBMITTED, _('Отправлено')),
    )
    template = models.CharField(max_length=50)
    email = models.CharField(max_length=1000)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    created = models.DateTimeField(auto_now=True)
    context = JSONField()

    objects = EmailDeliveryManager()

    class Meta:
        verbose_name = _('Письмо')
        verbose_name_plural = _('Письма')