from rest_framework.generics import ListAPIView
# Project imports
from product.models import Product, ProductProperty
from product.api import serializers


class ProductListAPIView(ListAPIView):
    serializer_class = serializers.ProductSerializer
    model = Product

    def get_queryset(self):
        qs = self.model.objects.get_list()
        qs = qs.prefetch_related('productproperty_set')
        return qs
