from rest_framework.generics import ListAPIView, RetrieveAPIView
# Project imports
from product.models import Product, ProductProperty
from product.api import serializers


class ProductList(ListAPIView):
    serializer_class = serializers.ProductSerializer
    model = Product

    def get_queryset(self):
        qs = self.model.objects.get_list()
        qs = qs.prefetch_related('productproperty_set')
        return qs


class ProductDetail(RetrieveAPIView):
    serializer_class = serializers.ProductSerializer
    model = Product

    def get_queryset(self):
        qs = self.model.objects.get_list()
        qs = qs.prefetch_related('productproperty_set')
        return qs


class ProductProperties(ListAPIView):
    serializer_class = serializers.ProductPropertySerializer
    model = ProductProperty

    def get_queryset(self):
        qs = self.model.objects.all()
        return qs
