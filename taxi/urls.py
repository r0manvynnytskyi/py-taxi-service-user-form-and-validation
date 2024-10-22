from django.urls import path
from .views import (
    index,
    CarListView,
    CarDetailView,
    CarCreateView,
    CarUpdateView,
    CarDeleteView,
    AssignMeToCarView,
    RemoveMeFromCarView,
    DriverListView,
    DriverDetailView,
    DriverCreateView,
    DriverDeleteView,
    DriverUpdateView,
    ManufacturerListView,
    ManufacturerCreateView,
    ManufacturerUpdateView,
    ManufacturerDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list",
    ),
    path(
        "manufacturers/create/",
        ManufacturerCreateView.as_view(),
        name="manufacturer-create",
    ),
    path(
        "manufacturers/<int:pk>/update/",
        ManufacturerUpdateView.as_view(),
        name="manufacturer-update",
    ),
    path("cars/<int:pk>/update/", CarUpdateView.as_view(), name="car-update"),
    path("cars/<int:pk>/delete/", CarDeleteView.as_view(), name="car-delete"),
    path(
        "cars/<int:pk>/assign-me/", AssignMeToCarView.as_view(), name="assign-me-to-car"
    ),
    path(
        "cars/<int:pk>/remove-me/",
        RemoveMeFromCarView.as_view(),
        name="remove-me-from-car",
    ),
    path("drivers/", DriverListView.as_view(), name="driver-list"),
    path("drivers/create/", DriverCreateView.as_view(), name="driver-create"),
    path("drivers/<int:pk>/delete/", DriverDeleteView.as_view(), name="driver-delete"),
    path("drivers/<int:pk>/update/", DriverUpdateView.as_view(), name="driver-update"),
    path("drivers/<int:pk>/", DriverDetailView.as_view(), name="driver-detail"),
]

app_name = "taxi"
