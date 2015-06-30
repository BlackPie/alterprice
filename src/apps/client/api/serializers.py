from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.core.validators import EMPTY_VALUES
from django.utils.crypto import constant_time_compare
from django.utils.translation import ugettext_lazy as _
User = get_user_model()
# Project imports
from client.api import messages
from catalog.models import EmailValidation, PasswordRecovery
from apuser import models


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
            raise serializers.ValidationError(_(u'Не валидная пара логин-пароль'))
        if not self.object.active():
            raise serializers.ValidationError(_(u'Не активный пользователь'))
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
        op_qs = models.OperatorProfile.objects.filter(code=code)
        models.ClientProfile.objects.make(
            user=user,
            operator=op_qs.first() if op_qs.exists() else None,
            city=validated_data.get('city'),
            company=validated_data.get('company'),
            name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            ownership_type=validated_data.get('ownership_type')
        )
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
        qs = User.objects.by_email(value)
        if qs.exists():
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
        qs = User.objects.by_email(value)
        if not qs.exists():
            raise serializers.ValidationError(
                messages.email_errors.get('not_exists'))
        rcvs = PasswordRecovery.objects.get_list(user=qs.first(), initial=True)
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
