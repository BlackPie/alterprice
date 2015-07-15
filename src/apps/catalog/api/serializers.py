from rest_framework import serializers
# Project imports
from catalog import models
from catalog.models.category import Category
from catalog.models.currency import Currency


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('codename', )
