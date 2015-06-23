from django.utils.translation import ugettext_lazy as _
from django.db import models
from utils.abstract_models import ApprovedModel, StatusModel, YMkey


class MakeException(Exception):
    ""


class ShopManager(models.Manager):
    def get_list(self):
        return self.all()

    def make(self, user):
        if not user.is_client():
            raise MakeException("Invalid user")
        return True


class Shop(ApprovedModel, StatusModel, YMkey):
    name = models.CharField(max_length=255,
                            verbose_name=_('Название'))
    user = models.ForeignKey('apuser.AlterPriceUser',
                             related_name='owner',
                             verbose_name=_('Пользователь'))
    entity = models.CharField(max_length=255,
                              verbose_name=_('Название юридического лица'))
    ogrn = models.CharField(max_length=255,
                            verbose_name=_('ОГРН'))
    city = models.ForeignKey('catalog.City',
                             null=True,
                             blank=True,
                             default=None,
                             verbose_name=_('Город'))
    phone = models.CharField(max_length=255,
                             null=True,
                             blank=True,
                             default=None,
                             verbose_name=_('Телефон'))
    address = models.CharField(max_length=255,
                               null=True,
                               blank=True,
                               default=None,
                               verbose_name=_('Адресс'))
    site = models.URLField(null=True,
                           blank=True,
                           default=None,
                           verbose_name=_('Сайт'))
    objects = ShopManager()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Магазин')
        verbose_name_plural = _('Магазины')
