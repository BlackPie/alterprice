from hashlib import md5
import logging

from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.core.validators import EMPTY_VALUES
from django.utils.crypto import constant_time_compare
from django.utils.translation import ugettext_lazy as _
from apuser.models.payment import InvoiceRequest, Payment
from catalog.models.token import EmailValidation, PasswordRecovery
from django.conf import settings

User = get_user_model()
from client.api import messages
from apuser import models


logger = logging.getLogger(__name__)


def create_username_field():
    username_field = User._meta.get_field(User.USERNAME_FIELD)
    mapping_dict = serializers.ModelSerializer.serializer_field_mapping
    field_class = mapping_dict[username_field.__class__]
    return field_class()


class SignInSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('password',)
        write_only_fields = ('password',)

    def __init__(self, *args, **kwargs):
        super(SignInSerializer, self).__init__(*args, **kwargs)
        self.fields[User.USERNAME_FIELD] = create_username_field()

    def validate(self, attrs):
        self.object = authenticate(username=attrs[User.USERNAME_FIELD],
                                   password=attrs['password'])
        if not self.object:
            raise serializers.ValidationError(_(u'Неверный email или пароль'))
        if not self.object.is_active:
            raise serializers.ValidationError(_(u'Пользователь не активен'))
        return attrs


class SignUpSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    phone = serializers.CharField(write_only=True)
    city = serializers.CharField(write_only=True)
    company = serializers.CharField(write_only=True, allow_blank=True, required=False)
    user_agreement = serializers.BooleanField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    ownership_type = serializers.ChoiceField(
        write_only=True,
        choices=models.ClientProfile.OWNERSHIP_CHOICES)

    operator_code = serializers.CharField(
        write_only=True,
        allow_blank=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'user_agreement',
                  'phone', 'first_name', 'last_name',
                  'city', 'ownership_type', 'company',
                  'operator_code', 'confirm_password')
        write_only_fields = [
            'phone', 'first_name', 'last_name', 'ownership_type',
            'city', 'company'
        ]

    def create(self, validated_data):
        email = validated_data.get('email')
        user = User.objects.make(
            email=email,
            password=validated_data.get('password'),)
        EmailValidation.objects.make(user=user, email=email)
        code = validated_data.get('operator_code')
        try:
            operator = models.OperatorProfile.objects.get(code=code)
        except models.OperatorProfile.DoesNotExist:
            operator = None
        client = models.ClientProfile.objects.make(
            user=user,
            operator=operator,
            city=validated_data.get('city'),
            company=validated_data.get('company'),
            name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            ownership_type=validated_data.get('ownership_type'))
        models.Balance.objects.make(client=client)
        return user

    def validate(self, attrs):
        pwd = attrs.get('password')
        confirm_pwd = attrs.get('confirm_password')
        if not constant_time_compare(pwd, confirm_pwd):
            raise serializers.ValidationError(_('Пароли не совпадают'))
        return attrs

    def validate_user_agreement(self, value):
        if not value:
            raise serializers.ValidationError(_('Необходимо согласие на хранение данных'))
        return value

    def validate_email(self, value):
        if value in EMPTY_VALUES:
            raise serializers.ValidationError(
                messages.email_errors.get('blank'))
        try:
            User.objects.get(email=value)
        except User.DoesNotExist:
            pass
        else:
            raise serializers.ValidationError(
                messages.email_errors.get('already_exist'))
        emvs = EmailValidation.objects.get_list(email=value)
        if emvs.exists():
            raise serializers.ValidationError(
                messages.email_errors.get('already_sent'))
        return value

    def validate_operator_code(self, value):
        if value not in EMPTY_VALUES:
            qs = models.OperatorProfile.objects.filter(code=value)
            if not qs.exists():
                raise serializers.ValidationError(
                    _('Оператор с таким кодом не найден'))
        return value


class RecoverySerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255,
                                   error_messages=messages.email_errors)

    def validate_email(self, value):
        if value in EMPTY_VALUES:
            raise serializers.ValidationError(
                messages.email_errors.get('blank'))
        try:
            u = User.objects.get(email=value)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                messages.email_errors.get('already_exist'))
        rcvs = PasswordRecovery.objects.get_list(user=u, initial=True)
        if rcvs.exists():
            raise serializers.ValidationError(
                messages.email_errors.get('already_sent'))
        return value


class RecoveryPasswordSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    token = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('password', 'confirm_password', 'token')

    def validate(self, attrs):
        pwd = attrs.get('password')
        confirm_pwd = attrs.get('confirm_password')
        if not constant_time_compare(pwd, confirm_pwd):
            raise serializers.ValidationError(_('Пароли не совпадают'))
        return attrs

    def validate_token(self, value):
        qs = PasswordRecovery.objects.get_valid(token=value)
        if not qs:
            raise serializers.ValidationError(_('Не валидный токен'))
        return value


class UpdateEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255,
                                   error_messages=messages.email_errors)
    new_email = serializers.EmailField(max_length=255,
                                   error_messages=messages.email_errors)

    def validate_email(self, value):
        if value in EMPTY_VALUES:
            raise serializers.ValidationError(messages.email_errors.get('blank'))
        if self.context['request'].user.email != value:
            raise serializers.ValidationError('Введенный email не совпадает с'
                                              ' email пользователя.')
        return value

    def validate_new_email(self, value):
        if value in EMPTY_VALUES:
            raise serializers.ValidationError(messages.email_errors.get('blank'))
        try:
            User.objects.get(email=value)
        except User.DoesNotExist:
            return value
        raise serializers.ValidationError(messages.email_errors.get('already_exist'))
        
        
class ProfileSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('phone',)

    def validate(self, attrs):
        phone = attrs.get('phone')
        if not phone:
            raise serializers.ValidationError(_('Укажите телефон'))
        return attrs


class ProfilePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True, max_length=128)
    old_password = serializers.CharField(write_only=True, max_length=128)

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(_('Пароль не подходит'))
        return value

    def validate(self, attrs):
        pwd = attrs.get('password')
        confirm_pwd = attrs.get('confirm_password')
        if not constant_time_compare(pwd, confirm_pwd):
            raise serializers.ValidationError({
                'confirm_password': _('Пароли не совпадают'),
            })
        return attrs


class InvoiceRequestAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = InvoiceRequest
        exclude = ('id', 'created', 'invoice_file', 'client')

    def create(self, validated_data):
        return InvoiceRequest(**validated_data)

    def get_file_attached(self, obj):
        return bool(obj.invoice_file)


class InvoiceRequestListSerializer(serializers.ModelSerializer):
    file_attached = serializers.SerializerMethodField()

    def get_file_attached(self, obj):
        return bool(obj.invoice_file)

    class Meta:
        model = InvoiceRequest
        fields = ('id', 'created', 'file_attached', 'invoice_file')


class RobokassaResultSerializer(serializers.Serializer):
    InvId = serializers.IntegerField()
    OutSum = serializers.FloatField()
    SignatureValue = serializers.CharField(max_length=60)

    def validate(self, attrs):
        try:
            Payment.objects.get(id=attrs.get('id'))
        except Payment.DoesNotExist:
            raise serializers.ValidationError(_('Не найден платеж с указанным идентификатором'))
        crc_txt = '%d:%d:%s' % (attrs.get('OutSum'), attrs.get('InvId'), settings.ROBOKASSA_PASS2, )
        crc = md5(crc_txt.encode('utf-8'))
        if str(crc.hexdigest()) != attrs.get('SignatureValue').lower():
            raise serializers.ValidationError(_('Контрольная сумма не совпадает'))
        return attrs


class RobokassaCreateSerializer(serializers.Serializer):
    OutSum = serializers.FloatField()