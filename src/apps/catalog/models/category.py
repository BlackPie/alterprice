import os
from django.db import models
from django.db.models import query
from django.utils.translation import ugettext_lazy as _
from marketapi.api import MarketAPI
from utils.abstract_models import NameModel, YMkey
from easy_thumbnails.fields import ThumbnailerField


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
            parent = None

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
    cached_product_photo = models.CharField(blank=True,
                                            null=True,
                                            default=None,
                                            max_length=255,
                                            verbose_name=_('Временное фото'))

    objects = CategoryManager.from_queryset(CategoryQuerySet)()

    def _get_thumbnail(self):
        if self.photo:
            try:
                return self.photo.url
            except AttributeError:
                pass

        return None


    def get_preview(self):
        '''
        Возвращает изображение категории или изображение
        рандомного товара одной из подкатегорий
        '''

        if self.depth == self.MAX_DEPTH_LEVEL:
            return None

        thumbnail = self._get_thumbnail()

        if thumbnail:
            url = thumbnail
        elif self.cached_product_photo:
            url = self.cached_product_photo
        else:
            category = self
            parents = [self]
            depth = self.depth
            url = None

            # если у текущей категории нет продуктов, проходимся по подкатегориям
            # пока не найдем категорию у которой есть продукты или не упрёмся
            # в самую нижнюю категорию
            while depth <= self.MAX_DEPTH_LEVEL:
                nonempty_category = Category.objects.filter(parent__in=parents)\
                                                    .filter(product__isnull=False)\
                                                    .order_by('?').first()
                if nonempty_category:
                    category = nonempty_category
                    break

                parents = Category.objects.filter(parent__in=parents)
                depth += 1

            try:
                # проходим по всем фото всех категорий пока не получим урл фото
                for product in category.product_set.order_by('?'):
                    if product.productphoto_set.all():
                        for photo in product.productphoto_set.order_by('?'):
                            if photo.photo.url:
                                url = photo.photo.url
                                self.cached_product_photo = url
                                self.save()
                    else:
                        continue

            except AttributeError:
                pass

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
