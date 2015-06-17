# -*- coding: utf-8 -*-
import django_filters
from django.core.validators import EMPTY_VALUES
from product.models import ProductShop


class DeliveryFilter(django_filters.NumberFilter):
    def filter(self, qs, value):
        # delivery_type=pickup
        # delivery_type=delivery
        if value not in EMPTY_VALUES:
            if value == 'pickup':
                return qs.filter(productshopdelivery__pickup=True)
            if value == 'delivery':
                return qs.filter(productshopdelivery__delivery=True)
        return qs


class ProductShopFilter(django_filters.FilterSet):
    delivery_type = DeliveryFilter()

    class Meta:
        model = ProductShop
        fields = ['delivery_type', ]
