import os
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.fields import ThumbnailerField
# from .product import Product
# from shop.models import OfferCategories
from catalog.models.currency import Currency
from catalog.models.property import Property


class OfferManager(models.Manager):
    def make_from_yml(self, yml_obj, shop, product, currency,
                      offercats, pricelist):
        obj = self.model()
        # check instances ( or useless method almost private)
        obj.product = product
        obj.shop = shop
        obj.currency = currency
        obj.pricelist = pricelist
        price = yml_obj.get('price')

        if '.' in price:
            price = float(price)
        obj.price = price
        for oc in offercats:
            if oc.category == product.category:
                obj.offercategory = oc
        obj.save()
        return obj


class Offer(models.Model):
    product = models.ForeignKey('product.Product',
                                verbose_name=_('Продукт'))
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

    objects = OfferManager()

    def __str__(self):
        return "%s: %s" % (self.shop.name, self.product.name)

    class Meta:
        verbose_name = _('Магазин продукта')
        verbose_name_plural = _('магазины продуктов')


class OfferDeliveryManager(models.Manager):
    def make_from_yml(self, productshop, yml_obj):
        obj = self.model()
        obj.productshop = productshop
        delivery_price = yml_obj.get('local_delivery_cost')
        if delivery_price:
            obj.price = int(delivery_price)
        obj.pickup = True if yml_obj.get('pickup') == 'true' else False
        obj.delivery = True if yml_obj.get('delivery') == 'true' else False
        obj.save()
        return obj


class OfferDelivery(models.Model):
    productshop = models.OneToOneField(Offer,
                                       verbose_name=_('Магазин продукта'))

    pickup = models.BooleanField(default=True,
                                 verbose_name=_('Самовывоз'))
    delivery = models.BooleanField(default=True,
                                   verbose_name=_('Доставка'))
    store = models.BooleanField(default=True,
                                verbose_name=_('Наличие'))
    price = models.IntegerField(null=True,
                                blank=True,
                                default=None,
                                verbose_name=_('Цена доставки'))

    objects = OfferDeliveryManager()

    class Meta:
        verbose_name = _('Доставка продукта')
        verbose_name_plural = _('Доставка продуктов')


class ProductPropertyManager(models.Manager):
    NON_PROPERTY_KEYS = (
        '',)

    def make(self, value, codename):
        obj = self.model()
        obj.value = value
        obj.prop = Property.objects.make(codename=codename)
        return obj

    def make_from_yml(self, yml_obj):
        pass


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


class ProductPhoto(models.Model):
    product = models.ForeignKey('product.Product',
                                verbose_name=_('Продукт'))
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
