from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import generic
from django.db.models import Q
from django.contrib import messages
from .models import Shipments


# Create your views here.
class ShipmentsListView(LoginRequiredMixin, generic.ListView):
    model = Shipments
    template_name = "shipments/shipments_list.html"
    queryset = Shipments.objects.all()
    paginate_by = 8

    def get_queryset(self):
        q = self.request.GET.get("q")
        if q:
            object_list = self.model.objects.filter(
                Q(created__icontains=q) | Q(label__icontains=q)
            )
        else:
            object_list = self.model.objects.all()
        return object_list


class ShipmentsDetailView(LoginRequiredMixin, generic.DetailView):
    model = Shipments
    context_object_name = "shipments"


class ShipmentsCreateView(LoginRequiredMixin, generic.CreateView):
    model = Shipments
    template_name = "shipments/shipments_form.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse("shipments:list-shipments")


class ShipmentsUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Shipments
    template_name = "shipments/shipments_form.html"
    fields = "__all__"

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("shipments:list-shipments")


class ShipmentsDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "delete_template.html"
    model = Shipments

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("shipments:list-shipments")
