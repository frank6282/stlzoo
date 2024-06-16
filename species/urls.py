from django.urls import path
from . import views

app_name = "species"

urlpatterns = [
    path("", views.SpeciesListView.as_view(), name="list-species"),
    path("create-species/", views.SpeciesCreateView.as_view(), name="create-species"),
    path(
        "species-detail/<int:pk>/",
        views.SpeciesDetailView.as_view(),
        name="detail-species",
    ),
    path(
        "update-species/<int:pk>/",
        views.SpeciesUpdateView.as_view(),
        name="update-species",
    ),
    path(
        "delete-species/<int:pk>/",
        views.SpeciesDeleteView.as_view(),
        name="delete-species",
    ),
]
