from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.views import generic
from .forms import SignupForm, LoginUserForm, PasswordChangingForm, EditUserProfileForm


class signup(SuccessMessageMixin, generic.CreateView):
    form_class = SignupForm
    template_name = "employees/register.html"
    success_url = reverse_lazy("login")
    success_message = "Your account has been successfully created. please login with username and password"

    def form_invalid(self, form):
        messages.add_message(
            self.request, messages.ERROR, "Please re-submit the form carefully"
        )
        return redirect("base")


class logIn(generic.View):
    form_class = LoginUserForm
    template_name = "employees/login.html"

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        if request.method == "POST":
            form = LoginUserForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")

                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    messages.success(request, f"You are logged in as {username}")
                    return redirect("base")
                else:
                    messages.error(request, "Error")
            else:
                messages.error(request, "Username or Password incorrect")
        form = LoginUserForm()
        return render(request, "employees/login.html", {"login_form": form})


class logOut(LoginRequiredMixin, generic.View):
    login_url = "login"

    def get(self, request):
        logout(request)
        messages.success(request, "user is logged out.")
        return redirect("base")


@login_required(login_url="login")
def profile(request):
    return render(request, "employees/profile.html")


class PasswordChangeView(PasswordChangeView):
    form_class = "PasswordChangingForm"
    success_url = reverse_lazy()


def password_success(request):
    return render(request, "employees/password_change_success.html")


class PasswordChngeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy("password_success")


class UpdateUserView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    form_class = EditUserProfileForm
    template_name = "employees/edit_user_profile.html"
    success_url = reverse_lazy("base")

    def get_object(self):
        return self.request.user

    def form_invalid(self, form):
        messages.add_message(
            self.request, messages.ERROR, "Please re-submit the form carefully"
        )
        return redirect("contact_us")


class DeleteUser(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = User
    template_name = "employees/delete_user_confirm.html"
    success_message = "User has been deleted"
    success_url = reverse_lazy("base")
