from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from djoser.serializers import TokenCreateSerializer
from rest_framework import serializers

from accounts.constants import CustomMessages as Messages
from accounts.models import Profile

User = get_user_model()


class TokenCreateSerializer(TokenCreateSerializer):
    default_error_messages = {
        'invalid_credentials': Messages.INVALID_CREDENTIALS_ERROR,
        'inactive_account': Messages.INACTIVE_ACCOUNT_ERROR,
        'suspend_account': Messages.SUSPEND_ACCOUNT_ERROR,
    }

    def validate(self, attrs):
        self.user = authenticate(
            username=attrs.get(User.USERNAME_FIELD),
            password=attrs.get('password')
        )
        print(self.user)
        self._validate_user_exists(self.user)
        self._validate_user_is_suspend(self.user)
        return attrs

    def _validate_user_is_suspend(self, user):
        if user.is_suspend:
            self.fail('suspend_account')


class AccountsUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            User.USERNAME_FIELD,
            'last_login',
            'date_joined',
            'is_active',
        )
        read_only_fields = (User.USERNAME_FIELD, 'is_active', 'last_login', 'date_joined')


# TODO: Change invalid choice message
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'mobile', 'bio', 'gender')
