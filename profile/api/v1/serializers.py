from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.compat import authenticate

from profile.models import *

# Create your serializers here.


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(label=_("Email"))
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('ایمیل / گذرواژه مورد تایید نیست.')
                raise serializers.ValidationError(
                    msg, code='authorization')
        else:
            msg = _('ایمیل و گذرواژه ضروریست.')
            raise serializers.ValidationError(
                msg, code='authorization')

        attrs['user'] = user
        return attrs


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
            },
        }

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            email=validated_data['email'], password=validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('url', 'username', 'email', 'last_login', 'date_joined')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('url', 'mobile', 'first_name', 'last_name', 'bio', 'gender',
                  'avatar', 'birth_date', 'country')
