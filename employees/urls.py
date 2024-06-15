from django.urls import path
from . import views

urlpatterns = [
    path("create-new-account/", views.signup.as_view(), name="register"),
    path("user-profile/", views.profile, name="profile"),
    path("login/", views.logIn.as_view(), name="login"),
    path("logout/", views.logOut.as_view(), name="logout"),
    path(
        "change_password/",
        views.PasswordChngeView.as_view(template_name="employees/password_change.html"),
        name="change-password",
    ),
    path(
        "password_success/",
        views.password_success,
        name="password_success",
    ),
    path("edit_profile/", views.UpdateUserView.as_view(), name="edit_user"),
    path("delete_user/<int:pk>/", views.DeleteUser.as_view(), name="delete_user"),
]
