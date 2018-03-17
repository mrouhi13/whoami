import djoser.views
from django.contrib.auth import get_user_model
from django.urls import path

from accounts.api.v1 import views

app_name = 'api.v1'

User = get_user_model()

urlpatterns = [
    path(
        'me/',
        views.ProfileView.as_view(),
        name='accounts'
    ),
    path(
        'account/',
        djoser.views.UserView.as_view(),
        name='account'
    ),
    path(
        'users/create/',
        djoser.views.UserCreateView.as_view(),
        name='user-create'
    ),
    path(
        'users/delete/',
        views.UserDeleteView.as_view(),
        name='user-delete'
    ),
    path(
        'users/activate/',
        views.ActivationView.as_view(),
        name='user-activate'
    ),
    path(
        '{0}/'.format(User.USERNAME_FIELD),
        views.SetUsernameView.as_view(),
        name='set_username'
    ),
    path(
        'password/',
        views.SetPasswordView.as_view(),
        name='set_password'
    ),
    path(
        'password/reset/',
        views.PasswordResetView.as_view(),
        name='password_reset'
    ),
    path(
        'password/reset/confirm/',
        views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    path(
        'token/create/',
        views.TokenCreateView.as_view(),
        name='token-create'
    ),
    path(
        'token/destroy/',
        views.TokenDestroyView.as_view(),
        name='token-destroy'
    ),
]
