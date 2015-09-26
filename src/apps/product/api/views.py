from django.core.validators import EMPTY_VALUES
from rest_framework.generics import ListAPIView
from django.db.models import Count, Q
# Project imports
from catalog.models.category import Category
from product import models
from product.api import serializers, filters
from product.models import Product, Opinion, Offer
from utils.views import APIView
from catalog.api.serializers import CategorySerializer


class ProductList(ListAPIView):
    serializer_class = serializers.ProductSerializer
    model = models.Product
    filter_class = filters.ProductListFilter

    def get_queryset(self):
        qs = self.model.objects.get_list()
        qs = qs.annotate(offers_count=Count('offer'))
        qs = qs.prefetch_related('offer_set')
        qs = qs.prefetch_related('productphoto_set')
        return qs


class ProductListCategories(ListAPIView):
    serializer_class = CategorySerializer
    model = Category
    filter_class = None

    def get_queryset(self):
        qs = models.Product.objects.get_list()
        qs = qs.annotate(offers_count=Count('offer'))
        qs = qs.prefetch_related('offer_set')
        qs = qs.prefetch_related('productphoto_set')
        f = filters.ProductListFilter(self.request.GET, queryset=qs)
        return self.model.objects.filter(product__in=f.qs).distinct()


class ProductCount(APIView):
    serializer_class = serializers.ProductCountSerializer

    def success_data(self, serializer):
        response = {}
        price_min = serializer.validated_data.get('price_min', None)
        price_max = serializer.validated_data.get('price_max', None)
        search = serializer.validated_data.get('search', None)
        category = serializer.validated_data.get('category')
        brand = serializer.validated_data.get('brand')

        qs = models.Product.objects.get_list()

        if price_min not in EMPTY_VALUES:
            qs = qs.by_min_price(price_min)

        if price_max not in EMPTY_VALUES:
            qs = qs.by_max_price(price_max)

        if category not in EMPTY_VALUES:
            qs = qs.by_category(category)
        if len(brand) > 0:
            qs = qs.by_brands(brand)

        if search not in EMPTY_VALUES:
            qs = qs.search(search)

        response['product_count'] = qs.distinct().count()
        return response


class ProductOffers(ListAPIView):
    serializer_class = serializers.OfferSerializer
    model = models.Offer
    filter_class = filters.OfferFilter

    def get_queryset(self):
        city_id = self.request.query_params.get('city', None)
        product_id = self.kwargs.get('pk', None)
        qs = self.model.objects.filter(product_id=product_id)

        if city_id:
            qs = qs.filter(pricelist__reqion=city_id)

        return qs


class SearchView(ListAPIView):
    model = Product
    serializer_class = serializers.ProductSerializer
    filter_class = filters.ProductSearchFilterSet

    def get_queryset(self):
        qs = self.model.objects.get_list()
        qs = qs.annotate(offers_count=Count('offer'))
        qs = qs.prefetch_related('offer_set')
        qs = qs.prefetch_related('productphoto_set')
        return qs

    def _search_categories(self):
        search = self.request.query_params.get('search', '')
        queryset = Category.objects.filter(Q(name__icontains=search)|
                                           Q(product__brand__name__icontains=search)|
                                           Q(product__name__icontains=search)).distinct()
        serializer = CategorySerializer(queryset, many=True)
        return serializer.data

    def get(self, *args, **kwargs):
        response = super(SearchView, self).get(*args, **kwargs)
        response.data['categories'] = self._search_categories()
        return response


class OpinionList(ListAPIView):
    model = Opinion
    serializer_class = serializers.OpinionSerializer
    filter_class = filters.OpinionFilterSet

    def get_queryset(self):
        return Opinion.objects.all()


class OfferSearchView(ListAPIView):
    model = Offer
    serializer_class = serializers.OfferSerializer

    def get_queryset(self):
        search = self.request.query_params.get('search', '')
        qs = self.model.objects.filter(product__isnull=True).filter(name__icontains=search)
        return qs
