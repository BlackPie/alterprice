import logging

from django.core.urlresolvers import reverse
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import status
from rest_framework.response import Response
# Project imports
from shop import models
from product import models as productmodels
from shop.api import serializers


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
    queryset = models.Shop.objects.all()
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
    model = models.Shop
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
    model = models.ShopYML

    def get_queryset(self):
        yml_id = self.kwargs.get('pk')
        qs = self.model.objects.filter(pk=yml_id)
        return qs

    def update(self, request, *args, **kwargs):
        response = {}
        instance = self.get_object()
        instance.published = True
        instance.save()
        response['status'] = 'success'
        api_status = status.HTTP_200_OK
        return Response(response, status=api_status)


class YMLUnPublish(UpdateAPIView):
    permission_classes = (IsAuthenticated, )
    model = models.ShopYML

    def get_queryset(self):
        yml_id = self.kwargs.get('pk')
        qs = self.model.objects.filter(pk=yml_id)
        return qs

    def update(self, request, *args, **kwargs):
        response = {}
        instance = self.get_object()
        instance.published = False
        instance.save()
        response['status'] = 'success'
        api_status = status.HTTP_200_OK
        return Response(response, status=api_status)


class YMLUpdate(UpdateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = serializers.YMLUpdateSerializer
    queryset = models.ShopYML.objects.all()

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
    queryset = models.ShopYML.objects.all()

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
    model = models.OfferCategories

    def get_queryset(self):
        yml_id = self.kwargs.get('pk')
        qs = self.model.objects.filter(shopyml_id=yml_id)
        return qs.select_related('category').order_by('category')


class YMLCategoryUpdate(UpdateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = models.OfferCategories.objects.all()
    serializer_class = serializers.YMLCategoryUpdateSerializer
    model = models.OfferCategories

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
    model = productmodels.ProductShop

    def get_queryset(self):
        yml_id = self.kwargs.get('pk')
        qs = self.model.objects.filter(shopyml_id=yml_id)
        # qs = qs.select_related('category')
        # qs = qs.prefetch_related('productshop_set')
        return qs.order_by('-product__category').distinct()
