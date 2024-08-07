from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from .forms import SignupForm, LoginUserForm, PasswordChangingForm, EditUserProfileForm


# Create your views here.
class signup(SuccessMessageMixin, generic.CreateView):
    form_class = SignupForm
    template_name = "authors/register.html"
    success_url = reverse_lazy("login")
    success_message = "User had been created, please login"

    def form_invalid(self, form):
        messages.add_message(
            self.request, messages.ERROR, "There was an error, re-submit"
        )
        return redirect("base")


class logIn(generic.View):
    form_class = LoginUserForm
    template_name = "authors/login.html"

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        if request.method == "POST":
            form = LoginUserForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]

                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    messages.success(request, f"You are logged in as {username}")
                    return redirect("home")
                else:
                    messages.error(request, "There was an error")
            else:
                messages.error(request, "Username or password incorrect")
        else:
            form = LoginUserForm()

        return render(request, "authors/login.html", {"form": form})


class logOut(generic.View):
    def get(self, request):
        logout(request)
        messages.success(request, "You have successfully logged out")
        return redirect("home")


class MyPasswordChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = "authors/password-change.html"
    success_url = reverse_lazy("password-change-done-view")


class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = "authors/password-reset-done.html"


class UpdateUserView(SuccessMessageMixin, generic.UpdateView):
    form_class = EditUserProfileForm
    template_name = "authors/edit_user_profile.html"
    success_url = reverse_lazy("home")
    success_message = "User had been updated"

    def get_object(self):
        return self.request.user

    def form_invalid(self, form):
        messages.add_message(
            self.request, messages.ERROR, "There was an error, re-submit"
        )
        return redirect("home")


class DeleteUser(SuccessMessageMixin, generic.DetailView):
    model = User
    template_name = "authors/delete_user_confirm.html"
    success_message = "User has been deleted"
    success_url = reverse_lazy("home")
