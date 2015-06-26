from django.core.urlresolvers import reverse
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework import status
from rest_framework.response import Response
# Project imports
from shop import models
from shop.api import serializers


class ShopCreate(CreateAPIView):
    permission_classes = (
        IsAuthenticated,
    )

    serializer_class = serializers.CreateShopSerializer

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
        # TODO: permission that only owner ( or admin can update shop)
        IsAuthenticated,
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
