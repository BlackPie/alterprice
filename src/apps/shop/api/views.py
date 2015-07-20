from collections import OrderedDict
from datetime import datetime, timedelta
import logging

from django.core.urlresolvers import reverse
from django.db.models import Sum, Count
from django.http import Http404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, \
    RetrieveAPIView
from rest_framework import status
from rest_framework.response import Response
# Project imports
from apuser.models import BalanceHistory
from product.models import ProductShop
from shop.api import serializers
from shop.models.offer import OfferCategories, Pricelist
from shop.models.shop import Shop

logger = logging.getLogger(__name__)


class ShopCreate(CreateAPIView):
    serializer_class = serializers.CreateShopSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        response = {}
        if serializer.is_valid():
            self.perform_create(serializer)
            response['status'] = 'success'
            response['redirect_to'] = reverse(
                'client:shop_detail',
                kwargs={"pk": serializer.instance.id})
            api_status = status.HTTP_201_CREATED
        else:
            response['status'] = 'fail'
            response['errors'] = serializer.errors
            api_status = status.HTTP_400_BAD_REQUEST
        return Response(response, status=api_status)


class ShopUpdate(UpdateAPIView):
    serializer_class = serializers.UpdateShopSerializer
    queryset = Shop.objects.all()
    permission_classes = (
        IsAuthenticated,
        # TODO: permission that only owner ( or admin can update shop)
    )

    def perform_update(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        response = {}
        if serializer.is_valid():
            self.perform_update(serializer)
            response['status'] = 'success'
            api_status = status.HTTP_200_OK
        else:
            response['status'] = 'fail'
            response['errors'] = serializer.errors
            api_status = status.HTTP_400_BAD_REQUEST
        return Response(response, status=api_status)


class ShopClientList(ListAPIView):
    serializer_class = serializers.ShopSerializer
    model = Shop
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return self.model.objects.by_owner(self.request.user)


class AddYML(CreateAPIView):
    serializer_class = serializers.YMLCreateSerialzier
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        # FIXIT TO shop from kwargs
        shop = self.request.user.get_shops().first()
        serializer.save(shop=shop)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        response = {}
        if serializer.is_valid():
            self.perform_create(serializer)
            response['status'] = 'success'
            response['redirect_to'] = reverse(
                'client:pricelist_detail',
                kwargs={"pk": serializer.instance.id})
            api_status = status.HTTP_201_CREATED
        else:
            response['status'] = 'fail'
            response['errors'] = serializer.errors
            api_status = status.HTTP_400_BAD_REQUEST
        return Response(response, status=api_status)


class YMLPublish(UpdateAPIView):
    permission_classes = (IsAuthenticated, )
    model = Pricelist

    def get_queryset(self):
        yml_id = self.kwargs.get('pk')
        qs = self.model.objects.filter(pk=yml_id)
        return qs

    def update(self, request, *args, **kwargs):
        response = {}
        instance = self.get_object()
        instance.publish_status = 1
        instance.save()
        response['status'] = 'success'
        api_status = status.HTTP_200_OK
        return Response(response, status=api_status)


class YMLUnPublish(UpdateAPIView):
    permission_classes = (IsAuthenticated, )
    model = Pricelist

    def get_queryset(self):
        yml_id = self.kwargs.get('pk')
        qs = self.model.objects.filter(pk=yml_id)
        return qs

    def update(self, request, *args, **kwargs):
        response = {}
        instance = self.get_object()
        instance.publish_status = 0
        instance.save()
        response['status'] = 'success'
        api_status = status.HTTP_200_OK
        return Response(response, status=api_status)


class YMLUpdate(UpdateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.YMLUpdateSerializer
    queryset = Pricelist.objects.all()

    def perform_update(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        response = {}
        if serializer.is_valid():
            self.perform_update(serializer)
            response['status'] = 'success'
            api_status = status.HTTP_200_OK
        else:
            response['status'] = 'fail'
            response['errors'] = serializer.errors
            api_status = status.HTTP_400_BAD_REQUEST

        return Response(response, status=api_status)


class YMLDelete(DestroyAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.YMLUpdateSerializer
    queryset = Pricelist.objects.all()

    def delete(self, request, pk):
        response = {}
        instance = self.get_object()
        instance.delete()
        response['status'] = 'success'
        response['redirect_to'] = reverse('client:profile')
        api_status = status.HTTP_200_OK
        return Response(response, status=api_status)


class YMLCategoryList(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.YMLCategoryListSerializer
    model = OfferCategories

    def get_queryset(self):
        yml_id = self.kwargs.get('pk')
        qs = self.model.objects.filter(pricelist_id=yml_id)
        return qs.select_related('category').order_by('category')


class YMLCategoryUpdate(UpdateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = OfferCategories.objects.all()
    serializer_class = serializers.YMLCategoryUpdateSerializer
    model = OfferCategories

    def perform_update(self, serializer):
        serializer.save()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        response = {}
        if serializer.is_valid():
            self.perform_update(serializer)
            response['status'] = 'success'
            api_status = status.HTTP_200_OK
        else:
            response['status'] = 'fail'
            response['errors'] = serializer.errors
            api_status = status.HTTP_400_BAD_REQUEST

        return Response(response, status=api_status)


class YMLProductList(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.YMLProductListserializer
    model = ProductShop

    def get_queryset(self):
        yml_id = self.kwargs.get('pk')
        qs = self.model.objects.filter(pricelist_id=yml_id)
        # qs = qs.select_related('category')
        # qs = qs.prefetch_related('productshop_set')
        return qs.order_by('-product__category').distinct()


class StatisticShop(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.StatisticSerializer

    def  _get_period_range(self, starting_point, day_num, duration):
        start = starting_point - timedelta(days=day_num)
        start = self._reset_time(start)
        end = start + timedelta(days=duration)
        return start, end

    def _reset_time(self, date):
        return date.replace(second=0, microsecond=0, minute=0, hour=0)

    def _get_period(self):
        now = datetime.now()
        period = self.request.query_params.get('period')
        if period == 'month':
            period_start, period_end = self._get_period_range(now, 30, 30)
        elif period == 'week':
            period_start, period_end = self._get_period_range(now, 7, 7)
        else:
            period_start, period_end = self._get_period_range(now, 1, 1)
        return period_start, period_end

    def _get_shop(self):
        try:
            return Shop.objects.get(pk=self.request.query_params.get('shop'))
        except Pricelist.DoesNotExist:
            raise Http404

    def get_queryset(self):
        period_start, period_end = self._get_period()
        return ProductShop.objects.filter(click__created__lt=period_end,
                                          click__created__gte=period_start,
                                          shop__user=self.request.user) \
            .annotate(sum=Sum('click__balancehistory__change_value'),
                      count=Count('click'))

    def get(self, request, *args, **kwargs):
        response = super(StatisticShop, self).get(request, *args, **kwargs)
        shop = self._get_shop()
        now = datetime.now()
        by_date = {}
        for x in range(7):
            start, end = self._get_period_range(now, x, 1)
            query = BalanceHistory.objects.filter(created__gte=start,
                                                  created__lt=end,
                                                  reason=BalanceHistory.CLICK,
                                                  click__productshop__shop=shop,
                                                  balance__client__user=self.request.user)
            clicks_count = query.count()
            money_sum = query.aggregate(Sum('change_value'))
            by_date.update({
                start.strftime('%d.%m.%y'): {
                    'clicks_count': clicks_count,
                    'money_sum': money_sum['change_value__sum'],
                }
            })
        response.data['by_date'] = by_date

        return response
