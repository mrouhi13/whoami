from django.contrib.auth import get_user_model
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
            'is_active',
        )
        read_only_fields = (
            User.USERNAME_FIELD, 'is_active', 'last_login', 'date_joined')


# TODO: Change invalid choice message
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'mobile', 'bio', 'gender')
