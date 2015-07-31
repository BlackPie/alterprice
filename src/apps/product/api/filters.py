# -*- coding: utf-8 -*-
import django_filters
from django.forms import ModelMultipleChoiceField
from django.core.validators import EMPTY_VALUES
# Project imports
from catalog.models.category import Category
from product import models
from brand.models import Brand
from product.models import Product, Opinion

EMPTY_VALUES = EMPTY_VALUES + ([''],)


class DeliveryFilter(django_filters.CharFilter):
    def filter(self, qs, value):
        if value not in EMPTY_VALUES:
            # TODO: update this shit
            if value == 'pickup':
                return qs.filter(productshopdelivery__pickup=True)
            if value == 'delivery':
                return qs.filter(productshopdelivery__delivery=True)
        return qs


class OfferFilter(django_filters.FilterSet):
    delivery_type = DeliveryFilter()

    class Meta:
        model = models.Offer
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
            return list()
        else:
            return super().clean(value)


class CategoryFilter(django_filters.ModelChoiceFilter):
    def filter(self, qs, value):
        if value not in EMPTY_VALUES:
            qs = qs.by_category(value)
        return qs


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


class ProductSearchFilterSet(django_filters.FilterSet):
    search = ProductSearchFilter()

    class Meta:
        model = models.Product
        fields = ['search']


class ProductListFilter(django_filters.FilterSet):
    price_max = PriceMaxFilter()
    price_min = PriceMinFilter()
    brand = BrandFilter(queryset=Brand.objects.all(),
                        required=False)
    category = CategoryFilter(queryset=Category.objects.all(), required=False)

    class Meta:
        model = models.Product
        fields = ['price_min', 'price_max', 'brand', 'category']


class OpinionProductFilter(django_filters.ModelChoiceFilter):
    def filter(self, qs, value):
        if value not in EMPTY_VALUES:
            qs = qs.filter(product=value)
        return qs


class OpinionFilterSet(django_filters.FilterSet):
    product = OpinionProductFilter(queryset=Product.objects.all(), required=True)

    class Meta:
        model = Opinion
        fields = ('product',)