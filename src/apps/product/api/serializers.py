from rest_framework import serializers
from django.core.urlresolvers import reverse
# Project imports
from catalog.models.category import Category
from product import models
from product.models import Opinion
from shop.api.serializers import ShopSerializer
from catalog.api.serializers import CategorySerializer
from brand.models import Brand


# class OfferDeliverySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.OfferDelivery
#         fields = ('delivery', 'pickup', 'price')


class OfferSerializer(serializers.ModelSerializer):
    shop = ShopSerializer()
    click_url = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = models.Offer
        fields = ('shop', 'price', 'click_url', 'delivery_cost', 'pickup', 'rating', 'name')

    def get_click_url(self, obj):
        return reverse('catalog:click-offer', kwargs={'pk': obj.id})

    def get_rating(self, obj):
        return obj.shop.raiting


class ProductSerializer(serializers.ModelSerializer):
    min_price = serializers.SerializerMethodField()
    offer = serializers.SerializerMethodField()
    offers_count = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()

    class Meta:
        model = models.Product
        fields = ('id', 'name', 'description', 'offer',
                  'min_price', 'offers_count', 'photo')

    def get_min_price(self, obj):
        ps = obj.get_offers().order_by('price').first()

        if ps:
            return ps.price
        else:
            return 0

    def get_offers_count(self, obj):
        return obj.offers_count

    def get_offer(self, obj):
        # Fix when top bets on category will released
        ps = obj.get_offers().first()
        return ShopSerializer(ps.shop).data if ps else None

    def get_photo(self, obj):
        p = obj.get_photos()
        return p.first().get_preview() if p.exists() else None


class ProductCountSerializer(serializers.Serializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        required=False,
        allow_null=True)
    brand = serializers.PrimaryKeyRelatedField(
        queryset=Brand.objects.all(),
        many=True)
    price_min = serializers.CharField(allow_blank=True, allow_null=True)
    price_max = serializers.CharField(allow_blank=True, allow_null=True)


class OpinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opinion
        exclude = ('ym_id', 'product')