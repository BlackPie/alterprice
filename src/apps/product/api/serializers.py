import random
from rest_framework import serializers
# Project imports
from product import models
from shop.api.serializers import ShopSerializer


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


class ProductPhotoSerializer(serializers.ModelSerializer):
    preview = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = models.ProductPhoto
        fields = ('preview', 'image')

    def get_preview(self, obj):
        return obj.get_preview()

    def get_image(self, obj):
        return obj.get_big()


class ProductShopDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductShopDelivery
        fields = ('delivery', 'pickup', 'price')


class ProductShopSerializer(serializers.ModelSerializer):
    shop = ShopSerializer()
    productshopdelivery = ProductShopDeliverySerializer()

    class Meta:
        model = models.ProductShop
        fields = ('shop', 'price', 'point', 'productshopdelivery')


class ProductSerializer(serializers.ModelSerializer):
    avg_price = serializers.SerializerMethodField()
    min_price = serializers.SerializerMethodField()
    max_price = serializers.SerializerMethodField()
    best_offer = serializers.SerializerMethodField()

    class Meta:
        model = models.Product
        fields = ('id', 'name', 'description', 'best_offer',
                  'avg_price', 'min_price', 'max_price')

    def get_avg_price(self, obj):
        return random.randrange(100, 10000)

    def get_min_price(self, obj):
        return random.randrange(20, 1000)

    def get_max_price(self, obj):
        return random.randrange(200, 1000)

    def get_best_offer(self, obj):
        ps = obj.productshop_set.first()
        return ProductShopSerializer(ps).data if ps else None
