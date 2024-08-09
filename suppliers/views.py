from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import generic
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Suppliers


# Create your views here.
class SuppliersListView(LoginRequiredMixin, generic.ListView):
    model = Suppliers
    queryset = Suppliers.objects.all()
    paginate_by = 8

    def get_queryset(self):
        q = self.request.GET.get("q")
        if q:
            object_list = self.model.objects.filter(
                Q(name__icontains=q) | Q(phone__icontains=q) | Q(country__icontains=q)
            )
        else:
            object_list = self.model.objects.all()
        return object_list


class SuppliersDetailView(LoginRequiredMixin, generic.DetailView):
    model = Suppliers
    context_object_name = "suppliers"


class SuppliersUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Suppliers
    template_name = "suppliers/suppliers_form.html"
    fields = "__all__"

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("suppliers:list-suppliers")


class SuppliersDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "delete_template.html"
    model = Suppliers

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("suppliers:list-suppliers")


class SuppliersCreateView(LoginRequiredMixin, generic.CreateView):
    model = Suppliers
    template_name = "suppliers/suppliers_form.html"
    fields = "__all__"

    success_url = "/"
