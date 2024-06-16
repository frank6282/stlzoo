from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("base.urls")),
    path("employees/", include("employees.urls")),
    path("contact_us/", include("contacts.urls")),
    path("species/", include("species.urls", namespace="species")),
    # Ckeditor
    path("ckeditor5/", include("django_ckeditor_5.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Stl-Insectarium"
admin.site.site_title = "Admin Page"
admin.site.index_title = "Welcome to the Admin Page"
