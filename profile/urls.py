from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

from profile.api.v1 import urls as v1_urls

# Create your urls here.


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('v1/', include(v1_urls, namespace='default')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
