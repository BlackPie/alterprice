import logging

from django.core.urlresolvers import reverse
from django.db.models import Sum, Count
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView,\
    DestroyAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from apuser.models.profile import EmailDelivery
from catalog.models.category import Category

from product.models import Offer
from shop.api import serializers
from shop.api.serializers import StatisticOfferSerializer, \
    StatisticCategorySerializer
from shop.models.offer import OfferCategories, Pricelist
from shop.models.shop import Shop
from .filters import StatisticOffersFilterSet, StatisticCategoriesFilterSet

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
            EmailDelivery.objects.make(
                template='client/shop_add.html',
                email=self.request.user.email
            )
            if self.request.user.client_profile.operator:
                EmailDelivery.objects.make(
                    template='operator/shop_add.html',
                    email=self.request.user.client_profile.operator.user.email
                )
        else:
            response['status'] = 'fail'
            response['errors'] = serializer.errors
            api_status = status.HTTP_400_BAD_REQUEST
        return Response(response, status=api_status)


class ShopUpdate(UpdateAPIView):
    serializer_class = serializers.UpdateShopSerializer
    permission_classes = (
        IsAuthenticated,
    )

    def get_queryset(self):
        return Shop.objects.filter(user=self.request.user)

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
        shop = Shop.objects.get(pk=self.kwargs['pk'])
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
    model = Offer

    def get_queryset(self):
        yml_id = self.kwargs.get('pk')
        qs = self.model.objects.filter(pricelist_id=yml_id).filter(product__isnull=False)
        # qs = qs.select_related('category')
        # qs = qs.prefetch_related('productshop_set')
        return qs.order_by('-product__category').distinct()


class StatisticOffers(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = StatisticOfferSerializer
    filter_class = StatisticOffersFilterSet

    def get_queryset(self):
        return Offer.objects.annotate(
            sum=Sum('click__balancehistory__change_value'),
            count=Count('click'),
        )


class StatisticCategories(ListAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = StatisticCategorySerializer
    filter_class = StatisticCategoriesFilterSet

    def get_queryset(self):
        return Category.objects.annotate(
            sum=Sum('product__offer__click__balancehistory__change_value'),
            count=Count('product__offer__click'),
        )


class YMLInfo(APIView):
    def get(self, *args, **kwargs):
        pricelist = Pricelist.objects.get(id=kwargs['pk'])
        product_offers = Offer.objects.filter(pricelist=pricelist).filter(product__isnull=False).distinct().count()
        unassigned_offers = Offer.objects.filter(pricelist=pricelist).filter(product__isnull=True).distinct().count()

        return Response({
            'product_offers': product_offers,
            'unassigned_offers': unassigned_offers
        })
