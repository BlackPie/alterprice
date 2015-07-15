from rest_framework.generics import ListAPIView
# Project imports
from catalog import models
from catalog.api import serializers
from catalog.models.category import Category


class CategoryList(ListAPIView):
    serializer_class = serializers.CategorySerializer
    model = Category

    def get_queryset(self):
        return self.model.objects.get_frist_level()
