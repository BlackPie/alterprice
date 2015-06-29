from rest_framework import serializers

from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.core.validators import EMPTY_VALUES
from django.utils.crypto import constant_time_compare
from django.utils.translation import ugettext_lazy as _
User = get_user_model()


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
        return attrs
