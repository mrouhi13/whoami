from django.contrib.auth.models import update_last_login
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from rest_framework import parsers, renderers, status
from rest_framework.views import APIView

from profile import viewsets
from profile.api.v1.serializers import *
from profile.models import AuthToken
from profile.response import response

# Create your views here.

sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters(
        'password', 'old_password', 'new_password1', 'new_password2'
    )
)


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser,
                      parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = AuthToken.objects.get_or_create(user=user)

        if token.expired():
            token.delete()
            token = AuthToken.objects.create(user=user)

        update_last_login(None, user)
        return response(content={'token': token.key},
                        status=status.HTTP_200_OK,
                        message='با موفقیت وارد شدید.')


class DisperseAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser,
                      parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)

    def post(self, request, *args, **kwargs):
        user = request.user
        token = AuthToken.objects.get(user=user)
        token.delete()
        return response(content={}, status=status.HTTP_200_OK,
                        message='با موفقیت خارج شدید.')


class PasswordReset(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser,
                      parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = PasswordResetSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response(content={},
                        status=status.HTTP_200_OK,
                        message="ایمیلی حاوی لینک بازیابی گذرواژه ارسال شد.")


class PasswordResetConfirm(APIView):
    """
    Password reset e-mail link is confirmed, therefore
    this resets the user's password.
    Accepts the following POST parameters: token, uid,
        new_password1, new_password2
    Returns the success/fail message.
    """
    serializer_class = PasswordResetConfirmSerializer
    permission_classes = ()

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super(PasswordResetConfirm, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response(content={},
                        status=status.HTTP_200_OK,
                        message="گذرواژه با موفقیت تغییر کرد.")


class RegisterNewUser(viewsets.ModelViewSet):
    """
    API endpoint that allows users to regsiter.
    """
    permission_classes = ()
    queryset = get_user_model().objects.all()
    serializer_class = UserRegisterSerializer
    http_method_names = ['post']
