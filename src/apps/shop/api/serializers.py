from rest_framework import serializers
# Project imports
from shop import models


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shop
        fields = ('id', 'name', 'approved')


class CreateShopSerializer(serializers.ModelSerializer):
    yml_url = serializers.CharField(allow_blank=True, write_only=True)
    yml_name = serializers.CharField(allow_blank=True, write_only=True)

    class Meta:
        model = models.Shop
        fields = ('city', 'phone', 'address', 'site', 'name', 'ogrn',
                  'entity', 'yml_name', 'yml_url')

    def create(self, validated_data):
        shop = models.Shop.objects.make(
            user=validated_data.get('user'),
            city=validated_data.get('city'),
            phone=validated_data.get('phone'),
            address=validated_data.get('address'),
            site=validated_data.get('site'),
            name=validated_data.get('name'),
            ogrn=validated_data.get('ogrn'),
            entity=validated_data.get('entity'))
        yml_url = validated_data.get('yml_url', None)
        if yml_url:
            models.ShopYML.objects.make(
                shop=shop,
                yml=yml_url,
                name=validated_data.get('yml_name'))
        return shop


class UpdateShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shop
        fields = ('phone', 'city', 'address', 'site')


class YMLCreateSerialzier(serializers.ModelSerializer):
    class Meta:
        model = models.ShopYML
        fields = ('yml_url', 'name')

    def create(self, validated_data):
        obj = models.ShopYML.objects.make(
            shop=validated_data.get('shop'),
            yml=validated_data.get('yml_url'),
            name=validated_data.get('name')
        )
        return obj
