from django.contrib.auth.models import update_last_login
from django.contrib.auth import get_user_model

from rest_framework import viewsets, permissions, parsers, renderers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken import views
from rest_framework.authtoken.models import Token

from profile.permissions import IsOwner
from profile.api.v1.serializers import *

# Create your views here.


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
        token, created = Token.objects.get_or_create(user=user)
        update_last_login(None, user)
        return Response({'token': token.key})


obtain_auth_token = ObtainAuthToken.as_view()


class RegisterNewUser(viewsets.ModelViewSet):
    """
    API endpoint that allows users to regsiter.
    """
    permission_classes = ()
    queryset = get_user_model().objects.all()
    serializer_class = UserRegisterSerializer
    http_method_names = ['post']


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed.
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get']

    def get_queryset(self):
        """
        This view should return a list of all the achievements
        for the currently authenticated user.
        """
        user = self.request.user
        return get_user_model().objects.filter(email=user)


class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows profiles to be viewed or edited.
    """
    permission_classes = (IsOwner, permissions.IsAuthenticated)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    http_method_names = ['get', 'put']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
        This view should return a profile for
        the currently authenticated user.
        """
        owner = self.request.user
        return Profile.objects.filter(owner=owner)
