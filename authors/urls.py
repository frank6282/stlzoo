from django.urls import path
from . import views

urlpatterns = [
    path(
        "change_password/",
        views.PasswordChangeView.as_view(template_name="authors/password_change.html"),
        name="change-password",
    ),
    path("create-new-account/", views.signup.as_view(), name="register"),
    path("login/", views.logIn.as_view(), name="login"),
    path("logout/", views.logOut.as_view(), name="logout"),
    path("user-profile/<str:user_name>/", views.profile.as_view(), name="profile"),
    path("delete_user/<int:pk>/", views.DeleteUser.as_view(), name="delete_user"),
]
