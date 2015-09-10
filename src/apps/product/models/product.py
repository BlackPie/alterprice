from django.core.validators import EMPTY_VALUES
from django.db import models
from django.db.models import query, Min, Max, Q
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields.json import JSONField
from catalog.models.category import Category
from marketapi.api import MarketAPI
from utils.abstract_models import YMkey
from brand.models import Brand


class ProductQuerySet(query.QuerySet):

    def active(self):
        return self.filter(
            offer__shop__user__client_profile__is_active=True,
            offer__pricelist__publish_status=1)

    def by_ymid(self, ym_id):
        # return self.active().filter(ym_id=ym_id)
        return self.filter(ym_id=ym_id)

    def by_min_price(self, value):
        qs = self.annotate(price_min=Min('offer__price'))
        return qs.filter(price_min__gte=value)

    def by_max_price(self, value):
        qs = self.annotate(price_max=Max('offer__price'))
        return qs.filter(price_max__lte=value)

    def by_brands(self, value):
        return self.filter(brand__in=value)

    def by_category(self, value):
        return self.filter(Q(category=value) |
                               Q(category__parent=value) |
                               Q(category__parent__parent=value) |
                               Q(category__parent__parent__parent=value) |
                               Q(category__parent__parent__parent__parent=value) |
                               Q(category__parent__parent__parent__parent__parent=value)
                               )

    def search(self, value):
        return self.filter(Q(name__icontains=value) |
                           Q(brand__name__icontains=value))


class ProductManager(models.Manager):

    def get_list(self):
        qs = self.active()
        return qs.distinct()

    def get_or_create(self, ym_id, brand_name, name, category_yml_id, description):
        try:
            return self.get(ym_id=ym_id)
        except self.model.DoesNotExist:
            return self.make(ym_id=ym_id,
                             brand_name=brand_name,
                             name=name,
                             category_yml_id=category_yml_id,
                             description=description)

    def make(self, ym_id, brand_name, name, category_yml_id, description):
        brand = Brand.objects.get_or_create(brand_name)
        category = Category.objects.get_or_create(ym_id=category_yml_id)

        if all((ym_id, brand_name, name, category_yml_id, description)):
            unfinished = False
        else:
            unfinished = True

        if not category:
            raise Exception('Cant create category with id "%d"' % category_yml_id)

        return self.create(
            ym_id=ym_id,
            brand=brand,
            name=name,
            category=category,
            description=description,
            details=self.get_details(ym_id),
            unfinished=unfinished
        )

    def get_details(self, ym_id):
        try:
            result = MarketAPI.get_model_detail(model_id=ym_id)['modelDetails']
        except:
            result = None

        return result


class Product(models.Model):
    ym_id = models.IntegerField(verbose_name=_('Yandex Market ID'),
                                blank=True,
                                null=True)
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
    loaded = models.BooleanField(default=True)
    unfinished = models.BooleanField(default=False,
                                     verbose_name='Нераспределённый товар')

    objects = ProductManager.from_queryset(ProductQuerySet)()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def get_photos(self):
        return self.productphoto_set.all()

    def get_offers(self):
        return self.offer_set.filter(shop__user__client_profile__is_active=True)

    def get_best_offer(self):
        offers = self.get_offers()
        return offers.first() if offers.exists() else None

    class Meta:
        verbose_name = _('Продукт')
        verbose_name_plural = _('Продукты')


class Opinion(models.Model):
    product = models.ForeignKey(Product)
    comment = models.CharField(max_length=10000, null=True, blank=True, verbose_name=_('Комментарий'))
    contra = models.CharField(max_length=10000, null=True, blank=True, verbose_name=_('Достоинства'))
    pro = models.CharField(max_length=10000, null=True, blank=True, verbose_name=_('Недостатки'))
    author = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('Имя автора'))
    grade = models.IntegerField(verbose_name=_('Оценка'))
    agree = models.IntegerField(verbose_name=_('Согласно'))
    reject = models.IntegerField(verbose_name=_('Не согласно'))
    date = models.DateTimeField(verbose_name=_('Дата создания'))
    ym_id = models.IntegerField(verbose_name=_('Market ID'), blank=True, null=True)

    class Meta:
        verbose_name = _('Отзыв')
        verbose_name_plural = _('Отзывы')

