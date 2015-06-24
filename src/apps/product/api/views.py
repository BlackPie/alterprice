from django.core.validators import EMPTY_VALUES
from rest_framework.generics import ListAPIView
from django.db.models import Count
# Project imports
from product import models
from product.api import serializers, filters
from utils.views import APIView
from catalog.models import Category
from catalog.api.serializers import CategorySerializer


class ProductList(ListAPIView):
    serializer_class = serializers.ProductSerializer
    model = models.Product
    filter_class = filters.ProductListFilter

    def get_queryset(self):
        qs = self.model.objects.get_list()
        qs = qs.annotate(offers_count=Count('productshop'))
        qs = qs.prefetch_related('productshop_set')
        qs = qs.prefetch_related('productphoto_set')
        return qs


class ProductListCategories(ListAPIView):
    serializer_class = CategorySerializer
    model = Category
    filter_class = None

    def get_queryset(self):
        qs = models.Product.objects.get_list()
        qs = qs.annotate(offers_count=Count('productshop'))
        qs = qs.prefetch_related('productshop_set')
        qs = qs.prefetch_related('productphoto_set')
        f = filters.ProductListFilter(self.request.GET, queryset=qs)
        return self.model.objects.filter(product__in=f.queryset)


class ProductCount(APIView):
    serializer_class = serializers.ProductCountSerializer

    def success_data(self, serializer):
        response = {}
        price_min = serializer.validated_data.get('price_min', None)
        price_max = serializer.validated_data.get('price_max', None)
        search = serializer.validated_data.get('search', None)
        category = serializer.validated_data.get('category')
        brand = serializer.validated_data.get('brand')

        qs = models.Product.objects.get_list()

        if price_min not in EMPTY_VALUES:
            qs = qs.by_min_price(price_min)

        if price_max not in EMPTY_VALUES:
            qs = qs.by_max_price(price_max)

        if category not in EMPTY_VALUES:
            qs = qs.by_category(category)
        if len(brand) > 0:
            qs = qs.by_brands(brand)

        if search not in EMPTY_VALUES:
            qs = qs.search(search)

        response['product_count'] = qs.distinct().count()
        return response


class ProductOffers(ListAPIView):
    serializer_class = serializers.ProductShopSerializer
    model = models.ProductShop
    filter_class = filters.ProductShopFilter

    def get_queryset(self):
        product_id = self.kwargs.get('pk', None)
        qs = self.model.objects.filter(product_id=product_id)
        return qs
