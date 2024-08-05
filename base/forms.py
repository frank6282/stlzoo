from django.contrib.auth.forms import AuthenticationForm


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
