from django.contrib import admin
from django.conf import settings
from django.urls import path, include
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]

if settings.DEBUG:  # Ensure Debug Toolbar is only added in debug mode
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
