import django_filters
from product.models import ProductShop
from shop.models import ShopYML


class ShopFilter(django_filters.ModelChoiceFilter):
    def filter(self, qs, value):
        qs.filter(shopyml=value)

class StatisticShopFilter(django_filters.FilterSet):
    shop = ShopFilter(queryset=ShopYML.objects.all())

    class Meta:
        model = ProductShop
        fields = ('shop')