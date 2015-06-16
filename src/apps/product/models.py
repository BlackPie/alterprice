import os
from django.db import models
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.fields import ThumbnailerField


class ProductManager(models.Manager):
    def get_list(self):
        qs = self.filter()
        return qs.distinct()


class Product(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name=_('Название'))
    created = models.DateTimeField(auto_now_add=True,
                                   editable=False,
                                   verbose_name=_(u'Дата создания'))
    description = models.TextField(verbose_name=_('Описание'))

    objects = ProductManager()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def get_photos(self):
        return self.productphoto_set.all()

    class Meta:
        verbose_name = _('Продукт')
        verbose_name_plural = _('Продукты')


class ProductFK(models.Model):
    product = models.ForeignKey(Product,
                                verbose_name=_('Продукт'))

    class Meta:
        abstract = True


class ProductShop(ProductFK):
    shop = models.ForeignKey('shop.Shop',
                             verbose_name=_('Магазин'))
    price = models.CharField(max_length=255,
                             verbose_name=_('Цена'))
    point = models.IntegerField(default=2,
                                verbose_name=_('Рейтинг'))

    class Meta:
        verbose_name = _('Магазин продукта')
        verbose_name_plural = _('магазины продуктов')


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
        if self.photo:
            return self.photo['product_small'].url
        else:
            return None

    def get_big(self):
        if self.photo:
            return self.photo['product_big'].url
        else:
            return None

    class Meta:
        verbose_name = _('Фото продукта')
        verbose_name_plural = _('Фото продуктов')