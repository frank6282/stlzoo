from django.urls import path
from django.contrib.auth import views as auth_views
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
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="authors/password_reset_form.html"
        ),
        name="password_reset",
    ),
    path(
        "password_reset_done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="authors/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password_reset_confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="authors/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password_reset_complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="authors/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path("create-new-account/", views.signup.as_view(), name="register"),
    #
    path("login/", views.logIn.as_view(), name="login"),
    path("logout/", views.logOut.as_view(), name="logout"),
    path("delete_user/<int:pk>/", views.DeleteUser.as_view(), name="delete_user"),
]
