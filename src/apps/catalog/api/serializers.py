from rest_framework import serializers
# Project imports
from catalog import models
from catalog.models.category import Category
from catalog.models.city import City
from catalog.models.currency import Currency


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('codename', )


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'slug')
