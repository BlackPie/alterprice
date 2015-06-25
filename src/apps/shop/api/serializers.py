from rest_framework import serializers
# Project imports
from shop import models


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shop
        fields = ('id', 'name', 'approved')


class CreateShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shop
