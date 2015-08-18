from django.db import models
from django.utils.translation import ugettext_lazy as _
from .category import Category


class CategoryStatistics(models.Model):
    category = models.ForeignKey(Category)
    created = models.DateField()
    click_count = models.PositiveIntegerField(verbose_name=_('Количество кликов'))
    shop_count = models.PositiveIntegerField(verbose_name=_('Количество магазинов'))
    product_count = models.PositiveIntegerField(verbose_name=_('Количество товаров'))

    def __str__(self):
        return "%s %s" % (self.category.name, self.created)

    class Meta:
        verbose_name = _('Статистика категории')
        verbose_name_plural = _('Статистика Категории')
