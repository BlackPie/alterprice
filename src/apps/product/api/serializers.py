import random
from rest_framework import serializers
# Project imports
from product.models import Product, ProductProperty


class ProductPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductProperty
        fields = ('property_name', 'property_value')


class ProductSerializer(serializers.ModelSerializer):
    avg_price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'avg_price')

    def get_avg_price(self, obj):
        return random.randrange(100, 10000)
