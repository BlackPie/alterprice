# -*- coding: utf-8 -*-
from django.forms import ModelMultipleChoiceField
import django_filters
from django.core.validators import EMPTY_VALUES
from product import models
from brand.models import Brand
from catalog.models import Category # NOQA
EMPTY_VALUES = EMPTY_VALUES + ([''],)


class DeliveryFilter(django_filters.CharFilter):
    def filter(self, qs, value):
        if value not in EMPTY_VALUES:
            if value == 'pickup':
                return qs.filter(productshopdelivery__pickup=True)
            if value == 'delivery':
                return qs.filter(productshopdelivery__delivery=True)
        return qs


class ProductShopFilter(django_filters.FilterSet):
    delivery_type = DeliveryFilter()

    class Meta:
        model = models.ProductShop
        fields = ['delivery_type', ]


class PriceMaxFilter(django_filters.NumberFilter):
    def filter(self, qs, value):
        if value not in EMPTY_VALUES:
            qs = qs.by_max_price(value)
        return qs


class PriceMinFilter(django_filters.NumberFilter):
    def filter(self, qs, value):
        if value not in EMPTY_VALUES:
            qs = qs.by_min_price(value)
        return qs


class ModelMultipleChoiceField(ModelMultipleChoiceField):
    def clean(self, value):
        if value in EMPTY_VALUES:
            return self.queryset
        else:
            return super().clean(value)


class BrandFilter(django_filters.ModelMultipleChoiceFilter):
    field_class = ModelMultipleChoiceField

    def filter(self, qs, value):
        if value not in EMPTY_VALUES:
            qs = qs.by_brands(value)
        return qs


class ProductSearchFilter(django_filters.CharFilter):
    def filter(self, qs, value):
        if value not in EMPTY_VALUES:
            qs = qs.search(value)
        return qs


class ProductListFilter(django_filters.FilterSet):
    price_max = PriceMaxFilter()
    price_min = PriceMinFilter()
    brand = BrandFilter(queryset=Brand.objects.all(),
                        required=False)
    # category = CategoryFilter(queryset=Category.objects.all())
    search = ProductSearchFilter()

    class Meta:
        model = models.Product
        # fields = ['price_min', 'price_max', 'brand', 'search', 'category']
        fields = ['price_min', 'price_max', 'brand', 'search']
