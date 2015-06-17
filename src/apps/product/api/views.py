from rest_framework.generics import ListAPIView
# Project imports
from product import models
from product.api import serializers, filters


class ProductList(ListAPIView):
    serializer_class = serializers.ProductSerializer
    model = models.Product

    def get_queryset(self):
        qs = self.model.objects.get_list()
        qs = qs.prefetch_related('productshop_set')
        return qs


class ProductOffers(ListAPIView):
    serializer_class = serializers.ProductShopSerializer
    model = models.ProductShop
    filter_class = filters.ProductShopFilter

    def get_queryset(self):
        product_id = self.kwargs.get('pk', None)
        qs = self.model.objects.filter(product_id=product_id)
        return qs
