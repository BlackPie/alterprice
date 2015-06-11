from django.db import models
from django.utils.translation import ugettext_lazy as _


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

    objects = ProductManager()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Продукт')
        verbose_name_plural = _('Продукты')


class ProductShop(models.Model):
    product = models.ForeignKey(Product,
                                verbose_name=_('Продукт'))
    shop = models.ForeignKey('shop.Shop',
                             verbose_name=_('Магазин'))
    price = models.CharField(max_length=255,
                             verbose_name=_('Цена'))

    class Meta:
        verbose_name = _('Магазин продукта')
        verbose_name_plural = _('магазины продуктов')


class ProductProperty(models.Model):
    product = models.ForeignKey(Product,
                                verbose_name=_('Продукт'))
    property_name = models.CharField(max_length=255,
                                     verbose_name=_('Название свойства'))
    property_value = models.CharField(max_length=255,
                                      verbose_name=_('Значение свойства'))

    def __str__(self):
        return "%s: %s" % (self.product, self.property_name)

    def __unicode__(self):
        return self.__str__

    class Meta:
        verbose_name = _('Свойство продукта')
        verbose_name_plural = _('Свойства продуктов')
