from rest_framework.generics import ListAPIView
# Project imports
from catalog import models
from catalog.api import serializers


class CategoryList(ListAPIView):
    serializer_class = serializers.CategorySerializer
    model = models.Category

    def get_queryset(self):
        return self.model.objects.get_frist_level()
