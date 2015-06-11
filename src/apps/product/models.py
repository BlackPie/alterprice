from django.db import models
from django.utils.translation import ugettext_lazy as _


class Product(models.Model):
    shop = models.ForeignKey('shop.Shop',
                             verbose_name=_('Магазин'))
    name = models.CharField(max_length=255,
                            verbose_name=_('Название'))
    created = models.DateTimeField(auto_now_add=True,
                                   editable=False,
                                   verbose_name=_(u'Дата создания'))

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Продукт')
        verbose_name_plural = _('Продукты')
