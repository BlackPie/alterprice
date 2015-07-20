import django_filters
from product.models import ProductShop
from shop.models.offer import Pricelist


class ShopFilter(django_filters.ModelChoiceFilter):
    def filter(self, qs, value):
        qs.filter(pricelist=value)

class StatisticShopFilter(django_filters.FilterSet):
    shop = ShopFilter(queryset=Pricelist.objects.all())

    class Meta:
        model = ProductShop
        fields = ('shop')