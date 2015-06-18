# -*- coding: utf-8 -*-
import django_filters
from django.core.validators import EMPTY_VALUES
from product import models
from brand.models import Brand
from catalog.models import Category
from django.db.models import Min, Max, Q


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
            # qs = qs.filter(productshop__price__lte=value)
            qs = qs.annotate(price_max=Max('productshop__price'))
            qs = qs.filter(price_max__lte=value)
        return qs


class PriceMinFilter(django_filters.NumberFilter):
    def filter(self, qs, value):
        if value not in EMPTY_VALUES:
            qs = qs.annotate(price_min=Min('productshop__price'))
            qs = qs.filter(price_min__gte=value)
        return qs


# class BrandFilter(django_filters.ModelChoiceFilter):
class BrandFilter(django_filters.ModelMultipleChoiceFilter):
    def filter(self, qs, value):
        if len(value) > 0:
            qs = qs.filter(brand__in=value)
        return qs


# class CategoryFilter(django_filters.ModelMultipleChoiceFilter):
#     def filter(self, qs, value):
#         return qs


class ProductSearchFilter(django_filters.CharFilter):
    def filter(self, qs, value):
        if value not in EMPTY_VALUES:
            qs = qs.filter(Q(name__icontains=value) | Q(brand__name__icontains=value))
        return qs


class ProductListFilter(django_filters.FilterSet):
    price_max = PriceMaxFilter()
    price_min = PriceMinFilter()
    brand = BrandFilter(queryset=Brand.objects.all())
    search = ProductSearchFilter()
    # category = CategoryFilter()

    class Meta:
        model = models.Product
        # fields = ['price_min', 'price_max', 'brand', 'search', 'category']
        fields = ['price_min', 'price_max', 'brand', 'search']
