from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordChangeForm,
    UserChangeForm,
)
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter your username"}
        )

        self.fields["first_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter your first name"}
        )

        self.fields["last_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter your last name"}
        )

        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter your email"}
        )

        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter your password"}
        )

        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Confirm your password"}
        )

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]

    username = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=150)
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()


class LoginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter your username"}
        )

        self.fields["password"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Enter your password"}
        )

    class Meta:
        fields = ["username", "password"]


class PasswordChangingForm(PasswordChangeForm):

    class Meta:
        model = User
        fields = ["old_password", "new_password1", "new_password2"]

    old_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Old Password"}
        )
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "New Password"}
        )
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirm Password"}
        )
    )


class EditUserProfileForm(UserChangeForm):

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your first name"}
        )
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your last name"}
        )
    )

    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter your last name"}
        ),
    )

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
