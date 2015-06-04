from django.db import models
from .apuser import AlterPriceUser
from django.utils.translation import ugettext_lazy as _


class AdminProfile(models.Model):
    user = models.OneToOneField(AlterPriceUser,
                                verbose_name=_('Пользователь'))

    class Meta:
        verbose_name = _('Профиль администратора')
        verbose_name_plural = _('Профили администраторов')


class OperatorProfile(models.Model):
    user = models.OneToOneField(AlterPriceUser,
                                verbose_name=_('Пользователь'))

    class Meta:
        verbose_name = _('Профиль оператора')
        verbose_name_plural = _('Профили операторов')


class ClientProfile(models.Model):
    user = models.OneToOneField(AlterPriceUser,
                                verbose_name=_('Пользователь'))

    class Meta:
        verbose_name = _('Профиль клиента')
        verbose_name_plural = _('Профили клиентов')
