from django.shortcuts import render, redirect

# Create your views here.
from django.contrib import messages
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.http import HttpResponse
from .forms import ContactForm
from .models import Contact


# Create your views here.
class contactUs(SuccessMessageMixin, generic.CreateView):
    form_class = ContactForm
    template_name = "contacts/contact_us.html"
    success_url = "/"

    def form_valid(self, form):
        fname = form.cleaned_data["first_name"]
        lname = form.cleaned_data["last_name"]

        send_mail(
            subject=f"From: {fname} {lname}",
            message=form.cleaned_data["contact_message"],
            recipient_list=["frankdil92@gmail.com"],
            from_email=None,
            fail_silently=False,
        )
        return super().form_valid(form)

    success_message = (
        "Your query has been submited successfully, we will contact you soon."
    )

    def form_invalid(self, form):
        messages.add_message(
            self.request, messages.ERROR, "Please re-submit the form carefully"
        )
        return redirect("contact_us")
