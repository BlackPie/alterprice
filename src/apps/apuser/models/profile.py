from django.db import models
from .apuser import AlterPriceUser
from django.utils.translation import ugettext_lazy as _
from utils.helpers import generate_code
from utils.abstract_models import ApprovedModel


class Profile(models.Model):
    user = models.OneToOneField(AlterPriceUser,
                                verbose_name=_('Пользователь'))
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

    class Meta:
        verbose_name = _('Администратор')
        verbose_name_plural = _('Администраторы')


class OperatorProfile(Profile):
    code = models.CharField(max_length=5,
                            default=generate_code,
                            verbose_name=_('Код'))

    class Meta:
        verbose_name = _('Оператор')
        verbose_name_plural = _('Операторы')


class ClientProfile(Profile, ApprovedModel):
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
