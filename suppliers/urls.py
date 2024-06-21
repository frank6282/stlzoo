from django.urls import path
from . import views

app_name = "suppliers"

urlpatterns = [
    path("", views.SuppliersListView.as_view(), name="list-suppliers"),
    path(
        "suppliers-detail/<int:pk>/",
        views.SuppliersDetailView.as_view(),
        name="detail-suppliers",
    ),
    path(
        "update-suppliers/<int:pk>/",
        views.SuppliersUpdateView.as_view(),
        name="update-suppliers",
    ),
    path(
        "delete-suppliers/<int:pk>/",
        views.SuppliersDeleteView.as_view(),
        name="delete-suppliers",
    ),
    path(
        "create-suppliers/",
        views.SuppliersCreateView.as_view(),
        name="create-suppliers",
    ),
]
