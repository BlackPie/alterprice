from rest_framework.generics import ListAPIView
# Project imports
from brand import models
from brand.api import serializers


class BrandList(ListAPIView):
    serializer_class = serializers.BrandSerializer
    model = models.Brand

    def get_queryset(self):
        return self.model.objects.all()
