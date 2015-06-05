from django.db import models
from .apuser import AlterPriceUser
from django.utils.translation import ugettext_lazy as _
from utils.helpers import generate_code


class AdminProfile(models.Model):
    user = models.OneToOneField(AlterPriceUser,
                                verbose_name=_('Пользователь'))

    class Meta:
        verbose_name = _('Профиль администратора')
        verbose_name_plural = _('Профили администраторов')


class OperatorProfile(models.Model):
    user = models.OneToOneField(AlterPriceUser,
                                verbose_name=_('Пользователь'))
    code = models.CharField(max_length=5,
                            default=generate_code,
                            verbose_name=_('Код'))

    class Meta:
        verbose_name = _('Профиль оператора')
        verbose_name_plural = _('Профили операторов')


class ClientProfile(models.Model):
    user = models.OneToOneField(AlterPriceUser,
                                verbose_name=_('Пользователь'))

    operator = models.ForeignKey(AlterPriceUser,
                                 null=True,
                                 blank=True,
                                 default=None,
                                 related_name='operator',
                                 verbose_name=_('Оператор'))

    class Meta:
        verbose_name = _('Профиль клиента')
        verbose_name_plural = _('Профили клиентов')
