import django_filters
from product.models import Offer
from shop.models.offer import Pricelist


PERIOD_CHOISES = (
    ('month', 'month'),
    ('week', 'week'),
    ('lastday', 'lastday'),
)

class PeriodFilter(django_filters.ChoiceFilter):
    def filter(self, qs, value):
        pass


class PricelistFilter(django_filters.ModelChoiceFilter):
    def filter(self, qs, value):
        qs.filter(pricelist=value)

class StatisticShopFilter(django_filters.FilterSet):
    period = PeriodFilter(queryset=Pricelist.objects.all())
