from rest_framework import serializers
# Project imports
from catalog import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('id', 'name')


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Currency
        fields = ('codename', )
