from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_pressure, name="add_pressure"),
    path("delete/<int:record_id>/", views.delete_pressure, name="delete_pressure"),
]