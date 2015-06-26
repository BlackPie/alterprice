from rest_framework import serializers
# Project imports
from apuser import models
from catalog.api.serializers import CurrencySerializer


class BillSerialziers(serializers.ModelSerializer):
    class Meta:
        model = models.Bill
        fields = ('amount', 'created')


class PaymentSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer()

    class Meta:
        model = models.Payment
        fields = ('payment_type', 'created', 'amount', 'currency')
