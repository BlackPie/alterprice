import random
from django.db.models import Min
from rest_framework import serializers
# Project imports
from product import models
from shop.api.serializers import ShopSerializer


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
    min_price = serializers.SerializerMethodField()
    offer = serializers.SerializerMethodField()
    offers_count = serializers.SerializerMethodField()

    class Meta:
        model = models.Product
        fields = ('id', 'name', 'description', 'offer',
                  'min_price', 'offers_count')

    def get_min_price(self, obj):
        price =  obj.productshop_set.filter(shop__status=1).aggregate(Min('price'))
        return price.get('price__min', None)

    def get_offers_count(self, obj):
        return obj.offers_count

    def get_offer(self, obj):
        ps = obj.productshop_set.order_by('price').first()
        return ProductShopSerializer(ps).data if ps else None
