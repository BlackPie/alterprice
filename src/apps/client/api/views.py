from rest_framework import permissions
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, get_user_model
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _
# Project imports
from client.api import serializers
from utils.views import APIView


class SignInAPIView(APIView):
    serializer_class = serializers.SignInSerializer
    permission_classes = (
        permissions.AllowAny,
    )

    def success_action(self, request, serializer):
        auth_login(request, serializer.object)

    def success_data(self, serializer):
        response = {}
        response['redirect_to'] = reverse_lazy('index')
        return response
