import random
from rest_framework import serializers
# Project imports
from product import models


class PropertyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PropertyInfo
        fields = ('property_name', 'property_value')


class ProductPropertySerializer(serializers.ModelSerializer):
    info = serializers.SerializerMethodField()

    class Meta:
        model = models.ProductProperty
        fields = ('name', 'info')

    def get_info(self, obj):
        qs = obj.propertyinfo_set.all()
        return PropertyInfoSerializer(qs, many=True).data


class ProductSerializer(serializers.ModelSerializer):
    avg_price = serializers.SerializerMethodField()

    class Meta:
        model = models.Product
        fields = ('id', 'name', 'description', 'avg_price')

    def get_avg_price(self, obj):
        return random.randrange(100, 10000)
