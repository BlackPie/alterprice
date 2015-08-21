import os
from django.db import models
from django.db.models import query
from django.utils.translation import ugettext_lazy as _
from marketapi.api import MarketAPI
from utils.abstract_models import NameModel, YMkey
from easy_thumbnails.fields import ThumbnailerField
# from apps.product.models.product import Product


class CategoryQuerySet(query.QuerySet):
    def by_ymid(self, ym_id):
        return self.filter(ym_id=ym_id)


class CategoryManager(models.Manager):
    def get_list(self):
        return self.all()

    def get_frist_level(self):
        qs = self.filter(parent__isnull=True)
        return qs.prefetch_related('children')

    def get_or_create(self, ym_id):
        try:
            return self.get(ym_id=ym_id)
        except self.model.DoesNotExist:
            return self.fetch_make(ym_id=ym_id)

    def fetch_make(self, ym_id):
        ym_category = MarketAPI.get_category(ym_id)['category']
        if 'parentId' in ym_category \
                and ym_category['parentId'] != 0 \
                and ym_category['parentId'] != 90401:
            parent = self.get_or_create(ym_category['parentId'])
            depth = parent.depth + 1
        else:
            depth = 0
            parent=None

        return self.create(
            name=ym_category['uniqName'],
            ym_id=ym_id,
            parent=parent,
            depth=depth,
        )

    def make(self, name, ym_id, parent=None):
        obj = self.model()
        obj.name = name
        obj.ym_id = ym_id
        obj.parent = parent
        obj.save()
        return obj



def get_photo_path(instance, filename):
    return os.path.join("category/", filename)


class Category(NameModel, YMkey):
    MAX_DEPTH_LEVEL = 4

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
    full_path = models.CharField(max_length=200, blank=True, null=True)

    objects = CategoryManager.from_queryset(CategoryQuerySet)()

    def get_preview(self):
        if self.depth == self.MAX_DEPTH_LEVEL:
            return None

        if self.photo:
            url = self.photo['category'].url
        else:
            try:
                url = self.product_set.order_by('?').first()\
                          .productphoto_set.order_by('?').first().photo.url
            except AttributeError:
                return None
            
        return url


    def get_children(self):
        return Category.objects.filter(parent=self.pk)

    def get_url(self):
        return "/catalog/%d/" % self.pk

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')
