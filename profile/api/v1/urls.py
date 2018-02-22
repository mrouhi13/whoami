from django.urls import path
from rest_framework.routers import DefaultRouter

from profile.api.v1 import views

# Create your urls here.

# Create a router and register our viewsets with it.
app_name = "profile"

router = DefaultRouter()
router.register('signup', views.RegisterNewUser)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('signin/', views.ObtainAuthToken.as_view()),
    path('signout/', views.DisperseAuthToken.as_view()),
    path('password-reset/', views.PasswordReset.as_view()),
    path('password-reset/confirm/', views.PasswordResetConfirm.as_view()),
] + router.urls
