from rest_framework import serializers
# Project imports
from product.models import Product, ProductProperty


class ProductPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductProperty
        fields = ('property_name', 'property_value')


class ProductSerializer(serializers.ModelSerializer):
    properties = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('name', 'properties')

    def get_properties(self, obj):
        qs = obj.productproperty_set.all()
        if qs.exists():
            return ProductPropertySerializer(qs, many=True).data
        else:
            return None
