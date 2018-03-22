from django.contrib.auth import get_user_model
from djoser import conf as djoser_conf
from rest_framework import serializers

from accounts.models import Profile

User = get_user_model()


class AccountsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            User.USERNAME_FIELD,
            'last_login',
            'date_joined',
        )
        read_only_fields = (User.USERNAME_FIELD, 'last_login', 'date_joined')


class TokenSerializer(serializers.ModelSerializer):
    token = serializers.CharField(source='key')

    class Meta:
        model = djoser_conf.settings.TOKEN_MODEL
        fields = ('token',)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'mobile', 'bio', 'gender')
