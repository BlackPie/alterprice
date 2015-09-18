import os
from urllib.request import urlopen
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.fields import ThumbnailerField
# from .product import Product
# from shop.models import OfferCategories
from catalog.models.currency import Currency
from catalog.models.property import Property
from django.core.files.temp import NamedTemporaryFile
from django.core.files.base import File


class OfferManager(models.Manager):
    pass


class Offer(models.Model):
    product = models.ForeignKey('product.Product',
                                verbose_name=_('Продукт'),
                                blank=True,
                                null=True)
    shop = models.ForeignKey('shop.Shop',
                             verbose_name=_('Магазин'))
    pricelist = models.ForeignKey('shop.Pricelist',
                                null=True,
                                blank=True,
                                default=None,
                                verbose_name=_('YML файл'))
    url = models.URLField(null=True,
                          blank=True,
                          default=None,
                          verbose_name=_('Ссылка на товар'))
    price = models.IntegerField(verbose_name=_('Цена'))
    click_price = models.IntegerField(
        default=settings.DEFAULT_CLICK_PRICE,
        verbose_name=_('Цена клика'))
    currency = models.ForeignKey(Currency,
                                 null=True,
                                 blank=True,
                                 default=None,
                                 verbose_name=_('Валюта'))
    offercategory = models.ForeignKey('shop.OfferCategories',
                                      null=True,
                                      blank=True,
                                      default=None,
                                      verbose_name=_('Категория предолжения'))
    delivery_cost = models.IntegerField(default=0)
    pickup = models.BooleanField(default=False)
    name = models.CharField(max_length=255,
                            null=True,
                            blank=True,
                            verbose_name=_('Название'))

    objects = OfferManager()

    def __str__(self):
        if self.product:
            name = "%s: %s" % (self.shop.name, self.product.name)
        else:
            name = "%s: %s" % (self.shop.name, self.name)
        return name

    class Meta:
        verbose_name = _('Магазин продукта')
        verbose_name_plural = _('магазины продуктов')


class ProductPropertyManager(models.Manager):
    NON_PROPERTY_KEYS = (
        '',)

    def make(self, value, codename):
        obj = self.model()
        obj.value = value
        obj.prop = Property.objects.make(codename=codename)
        return obj


class ProductProperty(models.Model):
    product = models.ForeignKey('product.Product',
                                verbose_name=_('Продукт'))
    value = models.CharField(max_length=255,
                             verbose_name=_('Значение свойства'))
    prop = models.ForeignKey(Property,
                             null=True,
                             blank=True,
                             default=None,
                             verbose_name=_('Свойство'))

    objects = ProductPropertyManager()

    def __str__(self):
        return "%s: %s" % (self.product, self.value)

    def __unicode__(self):
        return "%s: %s" % (self.product, self.value)

    class Meta:
        verbose_name = _('Свойство продукта')
        verbose_name_plural = _('Свойства продуктов')


def get_photo_path(instance, filename):
    return os.path.join("product/", filename)


class ProductPhotoManager(models.Manager):
    def make_from_url(self, url, product):
        extension = url.split('.')[-1]
        img_temp = NamedTemporaryFile(delete=True)
        img_temp.write(urlopen(url).read())
        img_temp.flush()
        obj = ProductPhoto(product=product)
        obj.photo.save('product_%d.%s' % (product.id, extension),
                       content=File(img_temp))
        obj.save()
        return obj


class ProductPhoto(models.Model):
    product = models.ForeignKey('product.Product',
                                verbose_name=_('Продукт'))
    photo = ThumbnailerField(blank=True,
                             null=True,
                             default=None,
                             upload_to=get_photo_path,
                             verbose_name=_('Фото'))

    objects = ProductPhotoManager()

    def get_preview(self):
        return self.photo['product_small'].url if self.photo else None

    def get_big(self):
        return self.photo['product_big'].url if self.photo else None

    class Meta:
        verbose_name = _('Фото продукта')
        verbose_name_plural = _('Фото продуктов')
