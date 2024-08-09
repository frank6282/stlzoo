from django.urls import path
from . import views

app_name = "shipments"

urlpatterns = [
    path("", views.ShipmentsListView.as_view(), name="list-shipments"),
    path(
        "shipments-detail/<int:pk>/",
        views.ShipmentsDetailView.as_view(),
        name="detail-shipments",
    ),
    path(
        "update-shipments/<int:pk>/",
        views.ShipmentsUpdateView.as_view(),
        name="update-shipments",
    ),
    path(
        "delete-shipments/<int:pk>/",
        views.ShipmentsDeleteView.as_view(),
        name="delete-shipments",
    ),
    path(
        "create-shipments/",
        views.ShipmentsCreateView.as_view(),
        name="create-shipments",
    ),
]
