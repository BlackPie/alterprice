from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
# Project imports
from apuser import models
from apuser.api import serializers


class PaymentList(ListAPIView):
    serializer_class = serializers.PaymentSerializer
    model = models.Payment
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return self.model.objects.by_user(self.request.user)
