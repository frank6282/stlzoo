from django.urls import path
from . import views

urlpatterns = [
    path("", views.contactUs.as_view(), name="contact_us"),
]
