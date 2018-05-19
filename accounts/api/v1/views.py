import djoser.compat
from django.contrib.auth import get_user_model
from djoser import utils, signals, conf as djoser_conf, views as djoser_views
from djoser.compat import get_user_email
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from accounts.api.v1.serializers import ProfileSerializer
from accounts.generics import CreateAPIView, RetrieveAPIView
from accounts.response import response

User = get_user_model()


class UserView(RetrieveAPIView):
    """
    Use this endpoint to retrieve user.
    """
    model = User
    serializer_class = djoser_conf.settings.SERIALIZERS.user
    permission_classes = [IsAuthenticated]

    def get_object(self, *args, **kwargs):
        return self.request.user

    def perform_update(self, serializer):
        super(UserView, self).perform_update(serializer)
        user = serializer.instance
        if djoser_conf.settings.SEND_ACTIVATION_EMAIL and not user.is_active:
            context = {'user': user}
            to = [get_user_email(user)]
            djoser_conf.settings.EMAIL.activation(self.request, context).send(to)


class UserCreateView(CreateAPIView):
    """
    Use this endpoint to register new user.
    """
    serializer_class = djoser_conf.settings.SERIALIZERS.user_create
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        signals.user_registered.send(
            sender=self.__class__, user=user, request=self.request
        )

        context = {'user': user}
        to = [get_user_email(user)]
        if djoser_conf.settings.SEND_ACTIVATION_EMAIL:
            djoser_conf.settings.EMAIL.activation(self.request, context).send(to)
        elif djoser_conf.settings.SEND_CONFIRMATION_EMAIL:
            djoser_conf.settings.EMAIL.confirmation(self.request, context).send(to)


class UserDeleteView(djoser_views.UserDeleteView):
    """
    Use this endpoint to remove actually authenticated user
    """

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)

        utils.logout_user(self.request)
        instance.delete()

        return response(status=status.HTTP_204_NO_CONTENT)


class TokenCreateView(djoser_views.TokenCreateView):
    """
    Use this endpoint to obtain user authentication token.
    """

    def _action(self, serializer):
        token = utils.login_user(self.request, serializer.user)
        token_serializer_class = djoser_conf.settings.SERIALIZERS.token
        return response(
            content={'token': token_serializer_class(token).data['auth_token'], 'is_active': serializer.user.is_active},
            status=status.HTTP_200_OK)


class TokenDestroyView(djoser_views.TokenDestroyView):
    """
    Use this endpoint to logout user (remove user authentication token).
    """

    def post(self, request):
        utils.logout_user(request)
        return response(status=status.HTTP_204_NO_CONTENT)


class PasswordResetView(djoser_views.PasswordResetView):
    """
    Use this endpoint to send email to user with password reset link.
    """

    def _action(self, serializer):
        for user in self.get_users(serializer.data['email']):
            self.send_password_reset_email(user)
        return response(status=status.HTTP_204_NO_CONTENT)


class SetUsernameView(djoser_views.SetUsernameView):
    """
    Use this endpoint to change user username.
    """

    def _action(self, serializer):
        user = self.request.user
        new_username = serializer.data['new_' + User.USERNAME_FIELD]

        setattr(user, User.USERNAME_FIELD, new_username)
        if djoser_conf.settings.SEND_ACTIVATION_EMAIL:
            user.is_active = False
            context = {'user': user}
            to = [djoser.compat.get_user_email(user)]
            djoser_conf.settings.EMAIL.activation(self.request, context).send(to)
        user.save()

        return response(status=status.HTTP_204_NO_CONTENT)


class SetPasswordView(djoser_views.SetPasswordView):
    """
    Use this endpoint to change user password.
    """

    def _action(self, serializer):
        self.request.user.set_password(serializer.data['new_password'])
        self.request.user.save()

        if djoser_conf.settings.LOGOUT_ON_PASSWORD_CHANGE:
            utils.logout_user(self.request)

        return response(status=status.HTTP_204_NO_CONTENT)


class PasswordResetConfirmView(djoser_views.PasswordResetConfirmView):
    """
    Use this endpoint to finish reset password process.
    """

    def _action(self, serializer):
        serializer.user.set_password(serializer.data['new_password'])
        serializer.user.save()
        return response(status=status.HTTP_204_NO_CONTENT)


class ActivationView(djoser_views.ActivationView):
    """
    Use this endpoint to activate user account.
    """

    def _action(self, serializer):
        user = serializer.user
        user.is_active = True
        user.save()

        signals.user_activated.send(
            sender=self.__class__, user=user, request=self.request
        )

        if djoser_conf.settings.SEND_CONFIRMATION_EMAIL:
            context = {'user': user}
            to = [djoser.compat.get_user_email(user)]
            djoser_conf.settings.EMAIL.confirmation(self.request, context).send(to)

        return response(status=status.HTTP_204_NO_CONTENT)


class ResendActivationEmailView(RetrieveAPIView):
    """
    Use this endpoint to retrieve user.
    """
    model = User
    serializer_class = djoser_conf.settings.SERIALIZERS.user
    permission_classes = [IsAuthenticated]

    def get_object(self, *args, **kwargs):
        return self.request.user

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        context = {'user': instance}
        to = [get_user_email(instance)]
        if djoser_conf.settings.SEND_ACTIVATION_EMAIL:
            djoser_conf.settings.EMAIL.activation(self.request, context).send(to)

        return response(status=status.HTTP_200_OK)


class ProfileView(generics.RetrieveUpdateAPIView):
    """
    Use this endpoint to retrieve/update accounts.
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return response(content=serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return response(content=serializer.data, status=status.HTTP_200_OK)
