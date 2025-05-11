from django.conf import settings
from django.contrib import admin
import django.urls

urlpatterns = [
    django.urls.path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += (
        django.urls.path(
            "__debug__/",
            django.urls.include("debug_toolbar.urls"),
        ),
    )
