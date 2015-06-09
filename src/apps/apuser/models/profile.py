from django.db import models
from .apuser import AlterPriceUser
from django.utils.translation import ugettext_lazy as _
from utils.helpers import generate_code
from utils.abstract_models import ApprovedModel


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

    class Meta:
        verbose_name = _('Оператор')
        verbose_name_plural = _('Операторы')


class ClientProfile(Profile, ApprovedModel):
    user = models.OneToOneField(AlterPriceUser,
                                related_name='client_user',
                                verbose_name=_('Пользователь'))
    operator = models.ForeignKey(AlterPriceUser,
                                 null=True,
                                 blank=True,
                                 default=None,
                                 related_name='operator',
                                 verbose_name=_('Оператор'))

    def __str__(self):
        return "%s" % self.user.email

    def __unicode__(self):
        return "%s" % self.user.email

    class Meta:
        verbose_name = _('Клиент')
        verbose_name_plural = _('Клиенты')
