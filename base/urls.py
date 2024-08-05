from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.logIn.as_view(), name="login"),
    path("logout/", views.logOut.as_view(), name="logout"),
]
