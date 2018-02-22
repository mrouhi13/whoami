from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from profile import views
from profile.api.v1 import urls as v1_urls

# Create your urls here.

app_name = 'profile'

# The API URLs are now determined automatically by the router.
urlpatterns = [
                  path('', views.index, name='index'),
                  path('profile/', views.profile, name='profile'),
                  path('signup/', views.signup, name='signup'),
                  path('signin/', views.signin, name='signin'),
                  path('password-reset/', views.password_reset, name='password_reset'),
                  path('password-reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
                  path('api/v1/', include(v1_urls, namespace='default')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
