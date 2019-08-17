from django.contrib.auth import get_user_model
from django.urls import path

from accounts.api.v1 import views

app_name = 'api.v1'

User = get_user_model()

urlpatterns = [
    path('me/', views.ProfileView.as_view(), name='profile'),
    path('account/', views.UserView.as_view(), name='account'),
    path('users/create/', views.UserCreateView.as_view(), name='user-create'),
    path('users/resend/', views.ResendActivationEmailView.as_view(),
         name='user-resend'),
    path('token/create/', views.TokenCreateView.as_view(),
         name='token-create'),
    path('token/destroy/', views.TokenDestroyView.as_view(),
         name='token-destroy'),
]
