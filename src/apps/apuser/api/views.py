from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
# Project imports
from apuser import models
from apuser.api import serializers
from apuser.models.payment import Payment, InvoiceRequest


class PaymentList(ListAPIView):
    serializer_class = serializers.PaymentSerializer
    model = Payment
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return self.model.objects.filter(client=self.request.user.client_profile)



class InvoiceList(ListAPIView):
    serializer_class = serializers.InvoiceSerializer
    model = InvoiceRequest
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return self.model.objects.filter(client=self.request.user.client_profile)
