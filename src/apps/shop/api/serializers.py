from rest_framework import serializers
# Project imports
from rest_framework.exceptions import ValidationError
from product.models import ProductShop
from shop import models
from product import models as productmodels
from catalog.api.serializers import CategorySerializer
from shop.models import Shop
from shop.models.offer import MakeException


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shop
        fields = ('id', 'name')


class CreateShopSerializer(serializers.ModelSerializer):
    yml_url = serializers.CharField(allow_blank=True, write_only=True)

    class Meta:
        model = models.Shop
        fields = ('city', 'phone', 'address', 'site', 'name', 'ogrn',
                  'entity', 'yml_url')

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
                yml=yml_url)
        return shop


class UpdateShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shop
        fields = ('phone', 'city', 'address', 'site')


class YMLCreateSerialzier(serializers.ModelSerializer):
    class Meta:
        model = models.ShopYML
        fields = ('yml_url', 'name', 'region_id')

    def create(self, validated_data):
        try:
            obj = models.ShopYML.objects.make(
                shop=validated_data.get('shop'),
                yml=validated_data.get('yml_url'),
                name=validated_data.get('name'),
                region_id=validated_data.get('region_id'),
            )
        except MakeException as e:
            raise ValidationError(str(e))
        return obj


class YMLCategoryListSerializer(serializers.ModelSerializer):
    lead_price = serializers.SerializerMethodField()
    category = CategorySerializer()

    class Meta:
        model = models.OfferCategories
        fields = ('id', 'category', 'price', 'lead_price')

    def get_lead_price(self, obj):
        try:
            max_price = models.OfferCategories.objects.filter(category=obj.category,
                              shopyml__shop__status=Shop.ENABLED) \
                .order_by('price')[0]
            return max_price.price
        except IndexError:
            return 0


class YMLCategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OfferCategories
        fields = ('price',)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = productmodels.Product
        fields = ('name', )


class YMLProductListserializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    product = ProductSerializer()

    class Meta:
        model = productmodels.ProductShop
        fields = ('product', 'category', 'click_price',)

    def get_category(self, obj):
        # or pass it trough CategorySerializer
        return obj.product.category.name


class YMLUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ShopYML
        fields = ('name', 'region_id')


class StatisticSerializer(serializers.Serializer):
    sum = serializers.IntegerField()
    count = serializers.IntegerField()
    name = serializers.CharField(source='product.name')
    id = serializers.IntegerField()
    category = serializers.IntegerField(source='product.category.id')

