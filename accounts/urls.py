from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from accounts import views
from accounts.api.v1 import urls as v1_urls

app_name = 'accounts'

urlpatterns = [
                  path('', views.index, name='index'),
                  path('me/', views.profile, name='profile'),
                  path('signup/', views.signup, name='signup'),
                  path('signin/', views.signin, name='signin'),
                  path('signup/successful/', views.signup_successful, name='signup_successful'),
                  path('password/reset/', views.password_reset, name='password_reset'),
                  path('password/reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
                  path('accounts/v1/', include(v1_urls, namespace='default')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
