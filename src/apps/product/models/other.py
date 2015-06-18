import os
from django.db import models
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.fields import ThumbnailerField
from .product import Product


class ProductFK(models.Model):
    product = models.ForeignKey(Product,
                                verbose_name=_('Продукт'))

    class Meta:
        abstract = True


class ProductShop(ProductFK):
    shop = models.ForeignKey('shop.Shop',
                             verbose_name=_('Магазин'))
    price = models.IntegerField(verbose_name=_('Цена'))
    point = models.IntegerField(default=2,
                                verbose_name=_('Рейтинг'))

    def __str__(self):
        return "%s: %s" % (self.shop.name, self.product.name)

    class Meta:
        verbose_name = _('Магазин продукта')
        verbose_name_plural = _('магазины продуктов')


class ProductShopDelivery(models.Model):
    productshop = models.OneToOneField(ProductShop,
                                       verbose_name=_('Магазин продукта'))

    pickup = models.BooleanField(default=True,
                                 verbose_name=_('Самовывоз'))
    delivery = models.BooleanField(default=True,
                                   verbose_name=_('Доставка'))
    price = models.IntegerField(null=True,
                                blank=True,
                                default=None,
                                verbose_name=_('Цена доставки'))

    class Meta:
        verbose_name = _('Доставка продукта')
        verbose_name_plural = _('Доставка продуктов')


class ProductProperty(ProductFK):
    name = models.CharField(max_length=255,
                            verbose_name=_('Название'))

    def __str__(self):
        return "%s: %s" % (self.product, self.name)

    def __unicode__(self):
        return "%s: %s" % (self.product, self.name)

    class Meta:
        verbose_name = _('Свойство продукта')
        verbose_name_plural = _('Свойства продуктов')


class PropertyInfo(models.Model):
    productproperty = models.ForeignKey(ProductProperty,
                                        verbose_name=_('Свойство'))
    property_name = models.CharField(max_length=255,
                                     verbose_name=_('Название свойства'))
    property_value = models.CharField(max_length=255,
                                      verbose_name=_('Значение свойства'))

    def __str__(self):
        return self.property_name

    def __unicode__(self):
        return self.property_name

    class Meta:
        verbose_name = _('Данные свойства')
        verbose_name_plural = _('Данные свойств')


def get_photo_path(instance, filename):
    return os.path.join("product/", filename)


class ProductPhoto(ProductFK):
    photo = ThumbnailerField(blank=True,
                             null=True,
                             default=None,
                             upload_to=get_photo_path,
                             verbose_name=_('Фото'))

    def get_preview(self):
        return self.photo['product_small'].url if self.photo else None

    def get_big(self):
        return self.photo['product_big'].url if self.photo else None

    class Meta:
        verbose_name = _('Фото продукта')
        verbose_name_plural = _('Фото продуктов')
