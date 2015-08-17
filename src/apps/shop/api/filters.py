from datetime import timedelta, datetime
import django_filters
from catalog.models.category import Category
from product.models import Offer
from shop.models.offer import Pricelist
from shop.models.shop import Shop

PERIOD_CHOICES = (
    ('month', 'month'),
    ('week', 'week'),
    ('lastday', 'lastday'),
)

class ShopFilter(django_filters.ModelChoiceFilter):
    def filter(self, qs, value):
        return qs.filter(shop=value)


class ShopCategoryFilter(django_filters.ModelChoiceFilter):
    def filter(self, qs, value):
        return qs.filter(product__offer__shop=value)


class PeriodClickFilter(django_filters.ChoiceFilter):
    def _get_period_range(self, starting_point, day_num, duration):
        start = starting_point - timedelta(days=day_num)
        start = self._reset_time(start)
        end = start + timedelta(days=duration)
        return start, end

    def _reset_time(self, date):
        return date.replace(second=0, microsecond=0, minute=0, hour=0)

    def _get_period(self, value):
        now = datetime.now()
        if value == 'month':
            period_start, period_end = self._get_period_range(now, 30, 30)
        elif value == 'week':
            period_start, period_end = self._get_period_range(now, 7, 7)
        else:
            period_start, period_end = self._get_period_range(now, 1, 1)
        return period_start, period_end

    def filter(self, qs, value):
        period_start, period_end = self._get_period(value)
        return qs.filter(click__created__lt=period_end,
                         click__created__gte=period_start)


class PeriodClickCategoryFilter(PeriodClickFilter):
    def filter(self, qs, value):
        period_start, period_end = self._get_period(value)
        return qs.filter(product__offer__click__created__lt=period_end,
                         product__offer__click__created__gte=period_start)


class PricelistFilter(django_filters.ModelChoiceFilter):
    def filter(self, qs, value):
        return qs.filter(pricelist=value)


class PricelistCategoryFilter(django_filters.ModelChoiceFilter):
    def filter(self, qs, value):
        return qs.filter(product__offer__pricelist=value)


class StatisticOffersFilterSet(django_filters.FilterSet):
    period = PeriodClickFilter(choices=PERIOD_CHOICES, required=True)
    shop = ShopFilter(queryset=Shop.objects.all())
    pricelist = PricelistFilter(queryset=Pricelist.objects.all())

    class Meta:
        model = Offer
        fields = ['period', 'pricelist', 'shop', ]


class StatisticCategoriesFilterSet(django_filters.FilterSet):
    period = PeriodClickCategoryFilter(choices=PERIOD_CHOICES, required=True)
    pricelist = PricelistCategoryFilter(queryset=Pricelist.objects.all())
    shop = ShopCategoryFilter(queryset=Shop.objects.all())

    class Meta:
        model = Category
        fields = ['period', 'pricelist', 'shop', ]
