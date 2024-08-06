from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views import generic
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Species


# Create your views here.
class SpeciesListView(LoginRequiredMixin, generic.ListView):
    model = Species
    template_name = "species/species_list.html"
    queryset = Species.objects.all()
    paginate_by = 8

    def get_queryset(self):
        q = self.request.GET.get("q")
        if q:
            object_list = self.model.objects.filter(
                Q(scientific_name__icontains=q) | Q(common_name__icontains=q)
            )
        else:
            object_list = self.model.objects.all()
        return object_list


class SpeciesDetailView(LoginRequiredMixin, generic.DetailView):
    model = Species
    context_object_name = "species"


class SpeciesCreateView(LoginRequiredMixin, generic.CreateView):
    model = Species
    template_name = "species/species_form.html"
    fields = ["scientific_name", "common_name", "description"]

    def get_success_url(self):
        return reverse("species:list-species")


class SpeciesUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Species
    template_name = "species/species_form.html"
    fields = ["scientific_name", "common_name", "description"]

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("species:list-species")


class SpeciesDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "delete_template.html"
    model = Species

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("species:list-species")
