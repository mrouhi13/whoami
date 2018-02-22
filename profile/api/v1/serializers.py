from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode as uid_decoder
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from rest_framework.compat import authenticate
from rest_framework.exceptions import ValidationError

from profile.models import *

# Create your serializers here.

UserModel = get_user_model()


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(label=_("ایمیل"), error_messages={
        'invalid': _('ایمیل وارد شده معتبر نیست.'),
        'required': _('ایمیل وارد نشده است.'),
        'null': _('ایمیل خالی است.'),
        'blank': _('ایمیل خالی است.')
    })
    password = serializers.CharField(
        label=_("گذرواژه"),
        style={'input_type': 'password'},
        trim_whitespace=False, error_messages={
            'invalid': _('گذرواژه وارد شده معتبر نیست.'),
            'required': _('وارد کردن گذرواژه الزامیست.'),
            'null': _('گذرواژه خالی است.'),
            'blank': _('گذرواژه خالی است.')
        })

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
                msg = _('ایمیل / گذرواژه اشتباه است.')
                raise serializers.ValidationError(
                    msg, code='authorization')
        else:
            msg = _('ایمیل / گذرواژه وارد نشده است.')
            raise serializers.ValidationError(
                msg, code='authorization')

        attrs['user'] = user
        return attrs


class PasswordResetSerializer(serializers.Serializer):
    """
    Serializer for requesting a password reset e-mail.
    """
    email = serializers.EmailField(label=_("ایمیل"), error_messages={
        'invalid': _('ایمیل وارد شده معتبر نیست.'),
        'required': _('ایمیل وارد نشده است.'),
        'null': _('ایمیل خالی است.'),
        'blank': _('ایمیل خالی است.')
    })

    password_reset_form_class = PasswordResetForm

    def get_email_options(self):
        """Override this method to change default e-mail options"""
        return {}

    def validate_email(self, value):
        # Create PasswordResetForm with the serializer
        self.reset_form = self.password_reset_form_class(data=self.initial_data)
        if not self.reset_form.is_valid():
            raise serializers.ValidationError(self.reset_form.errors)

        return value

    def save(self):
        request = self.context.get('request')
        # Set some values to trigger the send_email method.
        opts = {
            'use_https': request.is_secure(),
            'from_email': getattr(settings, 'DEFAULT_FROM_EMAIL'),
            'request': request,
            'email_template_name': 'profile/registration/password_reset_email.html',
        }

        opts.update(self.get_email_options())
        self.reset_form.save(**opts)


class PasswordResetConfirmSerializer(serializers.Serializer):
    """
    Serializer for requesting a password reset e-mail.
    """
    new_password1 = serializers.CharField(max_length=128)
    new_password2 = serializers.CharField(max_length=128)
    uid = serializers.CharField()
    token = serializers.CharField()

    set_password_form_class = SetPasswordForm

    def custom_validation(self, attrs):
        pass

    def validate(self, attrs):
        self._errors = {}

        # Decode the uidb64 to uid to get User object
        try:
            uid = force_text(uid_decoder(attrs['uid']))
            self.user = UserModel._default_manager.get(pk=uid)
        except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
            raise ValidationError({'uid': ['Invalid value']})

        self.custom_validation(attrs)
        # Construct SetPasswordForm instance
        self.set_password_form = self.set_password_form_class(
            user=self.user, data=attrs
        )
        if not self.set_password_form.is_valid():
            raise serializers.ValidationError(self.set_password_form.errors)
        if not default_token_generator.check_token(self.user, attrs['token']):
            raise ValidationError({'token': ['Invalid value']})

        return attrs

    def save(self):
        return self.set_password_form.save()


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(label=_("ایمیل"), error_messages={
        'unique': _("این ایمیل قبلا ثبت شده است."),
        'invalid': _('ایمیل وارد شده معتبر نیست.'),
        'required': _('ایمیل وارد نشده است.'),
        'null': _('ایمیل خالی است.'),
        'blank': _('ایمیل خالی است.')
    })
    password = serializers.CharField(
        label=_("گذرواژه"),
        style={'input_type': 'password'},
        trim_whitespace=False, error_messages={
            'invalid': _('گذرواژه وارد شده معتبر نیست.'),
            'required': _('وارد کردن گذرواژه الزامیست.'),
            'null': _('گذرواژه خالی است.'),
            'blank': _('گذرواژه خالی است.'),
            'unique': _("این ایمیل قبلا ثبت شده است.")
        })

    class Meta:
        model = UserModel
        fields = ('email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
            },
        }

    def create(self, validated_data):
        """
        Create and save a user with the given email and password.
        """
        if not validated_data['email']:
            raise ValueError('ایمیل وارد نشده است.')
        user = UserModel.objects.create(email=validated_data['email'], is_staff=False,
                                        is_superuser=False)
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('url', 'username', 'email', 'last_login', 'date_joined')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('url', 'mobile', 'first_name', 'last_name', 'bio', 'gender',
                  'avatar', 'birth_date', 'country')
