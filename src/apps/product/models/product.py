from django.core.validators import EMPTY_VALUES
from django.db import models
from django.db.models import query, Min, Max, Q
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields.json import JSONField
from catalog.models.category import Category
from utils.abstract_models import YMkey
from brand.models import Brand


class ProductQuerySet(query.QuerySet):

    def active(self):
        return self.filter(
            offer__shop__status=1,
            offer__pricelist__publish_status=1)

    def by_ymid(self, ym_id):
        # return self.active().filter(ym_id=ym_id)
        return self.filter(ym_id=ym_id)

    def by_min_price(self, value):
        qs = self.annotate(price_min=Min('productshop__price'))
        return qs.filter(price_min__gte=value)

    def by_max_price(self, value):
        qs = self.annotate(price_max=Max('productshop__price'))
        return qs.filter(price_max__lte=value)

    def by_brands(self, value):
        return self.filter(brand__in=value)

    def by_category(self, value):
        if value.children.exists():
            return self.filter(Q(category=value) | Q(category__in=value.children.all()))
        else:
            return self.filter(category=value)

    def search(self, value):
        return self.filter(Q(name__icontains=value) |
                           Q(brand__name__icontains=value))


class ProductManager(models.Manager):

    def get_list(self):
        qs = self.active()
        return qs.distinct()

    def get_name(self, yml_obj):
        if 'name' in yml_obj.keys():
            return yml_obj.get('name')
        if 'vendor' in yml_obj.keys():
            return yml_obj.get('model')

    def make_from_yml(self, yml_obj):
        ym_id = yml_obj.get('@id', None)
        if ym_id not in EMPTY_VALUES:
            qs = self.by_ymid(ym_id)
            if qs.exists():
                obj = qs.first()
            else:
                obj = self.model()
                obj.name = self.get_name(yml_obj)
                obj.ym_id = yml_obj.get('@id')
                category_id = yml_obj.get('categoryId')
                obj.category = Category.objects.by_ymid(category_id).first()
                obj.brand = Brand.objects.make_from_yml(yml_obj)
                obj.description = yml_obj.get('description')
                obj.save()
                # delivery
                # all other to properties!!
        return obj


class Product(YMkey):
    brand = models.ForeignKey('brand.Brand',
                              null=True,
                              blank=True,
                              default=None,
                              verbose_name=_('Бренд'))
    name = models.CharField(max_length=255,
                            verbose_name=_('Название'))
    created = models.DateTimeField(auto_now_add=True,
                                   editable=False,
                                   verbose_name=_(u'Дата создания'))
    category = models.ForeignKey('catalog.Category',
                                 null=True,
                                 blank=True,
                                 default=None,
                                 verbose_name=_('Категория'))
    description = models.TextField(null=True,
                                   blank=True,
                                   default=None,
                                   verbose_name=_('Описание'))
    details = JSONField(null=True, blank=True, verbose_name=_('Характеристики'))

    objects = ProductManager.from_queryset(ProductQuerySet)()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def get_photos(self):
        return self.productphoto_set.all()

    def get_offers(self):
        return self.offer_set.filter(shop__status=1)

    def get_best_offer(self):
        offers = self.get_offers()
        return offers.first() if offers.exists() else None

    class Meta:
        verbose_name = _('Продукт')
        verbose_name_plural = _('Продукты')


class Opinion(models.Model):
    product = models.ForeignKey(Product)
    comment = models.CharField(max_length=10000, null=True, blank=True, verbose_name=_('Комментарий'))
    contra = models.CharField(max_length=10000, null=True, blank=True, verbose_name=_('Недостатки'))
    pro = models.CharField(max_length=10000, null=True, blank=True, verbose_name=_('Достоинства'))
    author = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('Имя автора'))
    grade = models.IntegerField(verbose_name=_('Оценка'))
    agree = models.IntegerField(verbose_name=_('Согласно'))
    reject = models.IntegerField(verbose_name=_('Не согласно'))
    date = models.DateTimeField(verbose_name=_('Дата создания'))

