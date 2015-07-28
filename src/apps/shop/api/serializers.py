from rest_framework import serializers
# Project imports
from rest_framework.exceptions import ValidationError
from client.tasks import process_pricelist
from product.models import Offer
from shop import models
from product import models as productmodels
from catalog.api.serializers import CategorySerializer
from shop.models.offer import MakeException, OfferCategories, Pricelist
from shop.models.shop import Shop


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name')


class CreateShopSerializer(serializers.ModelSerializer):
    yml_url = serializers.CharField(allow_blank=True, write_only=True)

    class Meta:
        model = Shop
        fields = ('phone', 'address', 'site', 'name', 'ogrn',
                  'entity', 'yml_url', 'region')

    def create(self, validated_data):
        shop = Shop.objects.make(
            user=validated_data.get('user'),
            phone=validated_data.get('phone'),
            address=validated_data.get('address'),
            site=validated_data.get('site'),
            name=validated_data.get('name'),
            ogrn=validated_data.get('ogrn'),
            region=validated_data.get('region'),
            entity=validated_data.get('entity'))
        yml_url = validated_data.get('yml_url', None)
        if yml_url:
            Pricelist.objects.make(
                shop=shop,
                yml=yml_url,
                region=validated_data.get('region'),
            )
        return shop


class UpdateShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('phone', 'region', 'address', 'site')


class YMLCreateSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Pricelist
        fields = ('yml_url', 'name', 'region')

    def create(self, validated_data):
        try:
            obj = Pricelist.objects.make(
                shop=validated_data.get('shop'),
                yml_url=validated_data.get('yml_url'),
                name=validated_data.get('name'),
                region=validated_data.get('region'),
            )
            # process_pricelist.delay(pricelist_id=obj.id)
            process_pricelist(pricelist_id=obj.id)
        except MakeException as e:
            raise ValidationError(str(e))
        return obj


class YMLCategoryListSerializer(serializers.ModelSerializer):
    lead_price = serializers.SerializerMethodField()
    category = CategorySerializer()

    class Meta:
        model = OfferCategories
        fields = ('id', 'category', 'price', 'lead_price')

    def get_lead_price(self, obj):
        try:
            max_price = OfferCategories.objects.filter(category=obj.category,
                              pricelist__shop__status=Shop.ENABLED) \
                .order_by('price')[0]
            return max_price.price
        except IndexError:
            return 0


class YMLCategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferCategories
        fields = ('price',)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = productmodels.Product
        fields = ('name', )


class YMLProductListserializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    product_url = serializers.SerializerMethodField()
    product = ProductSerializer()

    class Meta:
        model = productmodels.Offer
        fields = ('product', 'category', 'click_price', 'product_url')

    def get_category(self, obj):
        # or pass it trough CategorySerializer
        return obj.product.category.name

    def get_product_url(self, obj):
        return "/product/detail/%d/" % obj.id


class YMLUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pricelist
        fields = ('name', 'region')


class StatisticSerializer(serializers.Serializer):
    sum = serializers.IntegerField()
    count = serializers.IntegerField()
    name = serializers.CharField(source='product.name')
    id = serializers.IntegerField()
    category = serializers.IntegerField(source='product.category.id')

