from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

from profile import views
from profile.api.v1 import urls as v1_urls

# Create your urls here.

app_name = 'profile'

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('recover-password', views.recover_password, name='recover_password'),
    path('agreement', views.agreement, name='agreement'),
    path('api/v1/', include(v1_urls, namespace='default')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)