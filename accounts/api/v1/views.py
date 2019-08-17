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
            djoser_conf.settings.EMAIL.activation(self.request, context).send(
                to)


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
            djoser_conf.settings.EMAIL.activation(self.request, context).send(
                to)
        elif djoser_conf.settings.SEND_CONFIRMATION_EMAIL:
            djoser_conf.settings.EMAIL.confirmation(self.request,
                                                    context).send(to)


class TokenCreateView(djoser_views.TokenCreateView):
    """
    Use this endpoint to obtain user authentication token.
    """

    def _action(self, serializer):
        token = utils.login_user(self.request, serializer.user)
        token_serializer_class = djoser_conf.settings.SERIALIZERS.token
        return response(
            content={'token': token_serializer_class(token).data['auth_token'],
                     'is_active': serializer.user.is_active},
            status=status.HTTP_200_OK)


class TokenDestroyView(djoser_views.TokenDestroyView):
    """
    Use this endpoint to logout user (remove user authentication token).
    """

    def post(self, request):
        utils.logout_user(request)
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
            djoser_conf.settings.EMAIL.activation(self.request, context).send(
                to)

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
        serializer = self.get_serializer(instance, data=request.data,
                                         partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return response(content=serializer.data, status=status.HTTP_200_OK)
