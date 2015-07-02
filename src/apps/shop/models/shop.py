from django.db import models
from django.db.models.query import QuerySet
from django.utils.translation import ugettext_lazy as _
from utils.abstract_models import StatusModel


class MakeException(Exception):
    ""


class ShopQuerySet(QuerySet):
    def by_owner(self, user):
        return self.filter(user=user)


class ShopManager(models.Manager):
    def get_list(self):
        return self.all()

    def make(self, user, name, ogrn, entity,
             phone=None, address=None, site=None, city=None):
        if not hasattr(user, 'is_client'):
            if not user.is_client():
                raise MakeException("Invalid user")
            raise MakeException("Invalid user")
        obj = self.model()
        obj.user = user
        obj.city = city
        obj.phone = phone
        obj.address = address
        obj.site = site
        obj.name = name
        obj.ogrn = ogrn
        obj.entity = entity
        obj.save()
        return obj

    def turn_off_debtor(self, user):
        qs = self.filter(user=user)
        if qs.exists():
            qs.update(status=Shop.DISABLED)


class Shop(StatusModel):
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

    objects = ShopManager.from_queryset(ShopQuerySet)()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def get_ymls(self):
        return self.shopyml_set.all()

    class Meta:
        verbose_name = _('Магазин')
        verbose_name_plural = _('Магазины')
