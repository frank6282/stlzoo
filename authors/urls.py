from django.urls import path
from . import views

urlpatterns = [
    path(
        "change-password/",
        views.MyPasswordChangeView.as_view(),
        name="password-change-view",
    ),
    path(
        "change-password/done/",
        views.MyPasswordResetDoneView.as_view(),
        name="password-change-done-view",
    ),
    path("create-new-account/", views.signup.as_view(), name="register"),
    path("login/", views.logIn.as_view(), name="login"),
    path("logout/", views.logOut.as_view(), name="logout"),
    path("delete_user/<int:pk>/", views.DeleteUser.as_view(), name="delete_user"),
]
