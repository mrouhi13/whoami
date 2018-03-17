from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from accounts.models import Profile

User = get_user_model()


# TODO: translate message to persian, custom djoser constants for all.
class AccountsUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            User.USERNAME_FIELD,
            'last_login',
            'date_joined',
        )
        read_only_fields = (User.USERNAME_FIELD, 'last_login', 'date_joined')


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'mobile', 'bio', 'birth_date', 'gender',
                  'avatar')
