from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from .forms import LoginUserForm, ContactForm


def home(request):
    return render(request, "base/home.html", {})


class logIn(generic.View):
    form_class = LoginUserForm
    template_name = "base/login.html"

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

        return render(request, "base/login.html", {"form": form})


class logOut(generic.View):
    def get(self, request):
        logout(request)
        messages.success(request, "You have successfully logged out")
        return redirect("home")


class contactUs(SuccessMessageMixin, generic.CreateView):
    form_class = ContactForm
    template_name = "base/contact_us.html"
    success_url = "/"
    success_message = "Your query has been submitted successfully"

    def form_invalid(self, form):
        messages.add_message(
            self.request, messages.ERROR, "There was an error, re-submit"
        )
        return redirect("home")
