from django.utils.translation import ugettext_lazy as _
from django.db import models


class MakeException(Exception):
    ""


class ShopManager(models.Manager):
    def get_list(self):
        return self.all()

    def make(self, user):
        if not user.is_client():
            raise MakeException("Invalid user")
        return True


class Shop(models.Model):
    user = models.ForeignKey('apuser.AlterPriceUser',
                             verbose_name=_('Пользователь'))

    objects = ShopManager()

    class Meta:
        verbose_name = _('Магазин')
        verbose_name_plural = _('Магазины')
