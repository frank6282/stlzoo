from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", include("admin_honeypot.urls", namespace="admin_honeypot")),
    path("theman/", admin.site.urls),
    path("", include("base.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "Stl-Insectarium"
admin.site.site_title = "Admin Page"
admin.site.index_title = "Welcome to the Admin Page"
