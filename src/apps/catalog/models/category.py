import os
from django.db import models
from django.utils.translation import ugettext_lazy as _
from utils.abstract_models import NameModel
from easy_thumbnails.fields import ThumbnailerField


class CategoryManager(models.Manager):
    def get_list(self):
        return self.all()

    def get_frist_level(self):
        qs = self.filter(parent__isnull=True)
        return qs.prefetch_related('children')


def get_photo_path(instance, filename):
    return os.path.join("category/", filename)


class Category(NameModel):
    parent = models.ForeignKey("self",
                               blank=True,
                               null=True,
                               related_name="children")
    click_count = models.IntegerField(default=0,
                                      verbose_name=_('Количество кликов'))
    shop_count = models.IntegerField(default=0,
                                     verbose_name=_('Количество магазинов'))
    goods_count = models.IntegerField(default=0,
                                      verbose_name=_('Количество товаров'))
    depth = models.IntegerField(default=0,
                                verbose_name=_('Глубина наследования'))
    photo = ThumbnailerField(blank=True,
                             null=True,
                             default=None,
                             upload_to=get_photo_path,
                             verbose_name=_('Фото'))

    objects = CategoryManager()

    def get_preview(self):
        return self.photo['category'].url if self.photo else None

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')
