from rest_framework import serializers
# Project imports
from brand import models


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Brand
        fields = ('id', 'name')
