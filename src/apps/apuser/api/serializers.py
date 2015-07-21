from rest_framework import serializers
# Project imports
from apuser import models
from apuser.models.payment import Payment, InvoiceRequest
from catalog.api.serializers import CurrencySerializer


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceRequest
        fields = ('id', 'amount')


class PaymentSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer()

    class Meta:
        model = Payment
        fields = ('payment_type', 'created', 'amount', 'currency')
