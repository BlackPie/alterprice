from django.db import models
from .apuser import AlterPriceUser
from django.utils.translation import ugettext_lazy as _
from utils.helpers import generate_code
from utils.abstract_models import ApprovedModel


class AdminProfile(models.Model):
    user = models.OneToOneField(AlterPriceUser,
                                verbose_name=_('Пользователь'))

    class Meta:
        verbose_name = _('Администратор')
        verbose_name_plural = _('Администраторы')


class OperatorProfile(models.Model):
    user = models.OneToOneField(AlterPriceUser,
                                verbose_name=_('Пользователь'))
    code = models.CharField(max_length=5,
                            default=generate_code,
                            verbose_name=_('Код'))

    class Meta:
        verbose_name = _('Оператор')
        verbose_name_plural = _('Операторы')


class ClientProfile(ApprovedModel):
    user = models.OneToOneField(AlterPriceUser,
                                verbose_name=_('Пользователь'))

    operator = models.ForeignKey(AlterPriceUser,
                                 null=True,
                                 blank=True,
                                 default=None,
                                 related_name='operator',
                                 verbose_name=_('Оператор'))

    def __str__(self):
        return self.user.name

    def __unicode__(self):
        return self.user.name

    class Meta:
        verbose_name = _('Клиент')
        verbose_name_plural = _('Клиенты')
