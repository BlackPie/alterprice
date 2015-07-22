import logging
from hashlib import md5

from rest_framework import permissions
from rest_framework import status
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListCreateAPIView, \
    ListAPIView
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth import login as auth_login
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.hashers import make_password
from apuser.models import BalanceHistory

from apuser.models.payment import InvoiceRequest, Payment
from apuser import models
from catalog.models.token import PasswordRecovery
from client.api import serializers
from django.conf import settings
from utils.views import APIView
from django.contrib.auth import update_session_auth_hash


logger = logging.getLogger(__name__)


class SignInAPIView(APIView):
    serializer_class = serializers.SignInSerializer
    permission_classes = (permissions.AllowAny, )

    def success_action(self, request, serializer):
        auth_login(request, serializer.object)

    def success_data(self, serializer):
        response = {}
        response['redirect_to'] = reverse_lazy('client:profile')
        return response


class SignUpAPIView(CreateAPIView):
    serializer_class = serializers.SignUpSerializer
    permission_classes = (
        permissions.AllowAny,
    )

    def perform_create(self, serializer):
        serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        response = {}
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            response['status'] = 'success'
            response['message'] = _('Для завершения регистрации перейдите по ссылке из письма отправленного на ваш e-mail. Если не найдете во входящих, проверьте "спам"')
            return Response(response, status=status.HTTP_201_CREATED, headers=headers)
        else:
            response['status'] = 'fail'
            response['errors'] = serializer.errors
            headers = self.get_success_headers(serializer.data)
            return Response(response,
                            status=status.HTTP_400_BAD_REQUEST,
                            headers=headers)


class Recovery(APIView):
    serializer_class = serializers.RecoverySerializer
    permission_classes = (
        permissions.AllowAny,
    )

    def success_action(self, request, serializer):
        email = serializer.validated_data.get('email')
        user = models.AlterPriceUser.objects.get(email=email)
        PasswordRecovery.objects.make(user=user)

    def success_data(self, serializer):
        response = {}
        # email = serializer.validated_data.get('email')
        response['message'] = _(
            'Выслано сообщение со ссылкой на восстановление')
        return response


class RecoveryPassword(APIView):
    serializer_class = serializers.RecoveryPasswordSerializer
    permission_classes = (permissions.AllowAny, )

    def success_action(self, request, serializer):
        password = serializer.validated_data.get('password')
        pr = PasswordRecovery.objects.get_valid(
            token=serializer.validated_data.get('token'))
        pr.recover()
        user = pr.user
        user.set_password(password)
        user.save()

    def success_data(self, serializers):
        response = {}
        response['message'] = _('Ваш пароль был успешно изменен.')
        response['redirect_to'] = reverse('client:login')
        return response


class UpdateEmail(APIView):
    serializer_class = serializers.UpdateEmailSerializer
    permission_classes = (permissions.AllowAny, )

    def success_action(self, request, serializer):
        self.request.user.email = serializer.validated_data.get('new_email')
        self.request.user.save()

    def success_data(self, serializers):
        response = {}
        response['message'] = _('Ваш email был успешно изменен.')
        response['status'] = 'success'
        return response


class InvoiceListView(ListAPIView):
    model = InvoiceRequest
    serializer_class = serializers.InvoiceRequestListSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def get_queryset(self):
        queryset = super(InvoiceListView, self).get_queryset()
        queryset.filter(client=self.request.user.client_profile)
        return queryset


class InvoiceCreateView(CreateAPIView):
    serializer_class = serializers.InvoiceRequestAddSerializer
    permission_classes = (permissions.IsAuthenticated, )
    model = InvoiceRequest

    def get_queryset(self):
        return self.model.objects.filter(client=self.request.user.client_profile)

    def perform_create(self, serializer):
        ir = serializer.save()
        ir.client = self.request.user.client_profile
        ir.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        response = {}
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            response['status'] = 'success'
            response['message'] = _('Запрос на счет отправлен.')
            return Response(response, status=status.HTTP_201_CREATED, headers=headers)
        else:
            response['status'] = 'fail'
            response['errors'] = serializer.errors
            headers = self.get_success_headers(serializer.data)
            return Response(response,
                            status=status.HTTP_400_BAD_REQUEST,
                            headers=headers)


class Profile(APIView):
    serializer_class = serializers.ProfileSerializer

    def success_action(self, request, serializer):
        phone = serializer.validated_data.get('phone')
        request.user.client_profile.phone = phone
        request.user.client_profile.save()

    def success_data(self, serializers):
        response = {}
        response['status'] = 'success'
        return response


class ProfilePassword(APIView):
    serializer_class = serializers.ProfilePasswordSerializer

    def success_action(self, request, serializer):
        password = serializer.validated_data.get('password')
        request.user.set_password(password)
        request.user.save()
        update_session_auth_hash(request, request.user)

    def success_data(self, serializers):
        response = {}
        response['status'] = 'success'
        response['message'] = _('Ваш пароль успешно изменен')
        return response


class RobokassaResultAPIView(APIView):
    serializer_class = serializers.RobokassaResultSerializer
    renderer_classes = (StaticHTMLRenderer, )

    def post(self, request, *args, **kwargs):
        data = self.prepare_data(request)
        serializer = self.serializer_class(data=data, context=dict(request=request))
        response = ''
        if serializer.is_valid():
            payment_id = serializer.validated_data.get('InvId')
            payment = Payment.objects.get(id=payment_id)
            payment.robokassa_success = True
            payment.save()
            BalanceHistory.objects.increase(
                balance=payment.client.balance,
                payment=payment,
            )
            self.success_action(request, serializer)
            response = 'OK%d' % payment_id
        return Response(response, status=200)


class RobokassaCreatePaymentAPIView(APIView):
    model = Payment
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self):
        payment = self.model(
            client=self.request.user.client_profile,
            # amount=serializer.validated_data.get('OutSum'),
            payment_type=Payment.ONLINE,
            payment_detail=Payment.PAYMENT,
        )
        payment.save()
        return payment

    def post(self, request, *args, **kwargs):
        payment = self.perform_create()
        crc_txt = '%s::%d:%s' % (settings.ROBOKASSA_LOGIN, payment.id, settings.ROBOKASSA_PASS1, )
        response = {
            'crc': md5(crc_txt.encode('utf-8')),
            'id': payment.id,
        }
        return Response(response, status=201)