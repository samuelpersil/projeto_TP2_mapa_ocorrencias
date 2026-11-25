"""Roteamento de URLs da aplicação notifications."""

from django.urls import path

from apps.notifications import views

app_name = "notifications"

urlpatterns = [
    path("", views.inbox_view, name="inbox"),
    path(
        "seguir/ocorrencia/<int:incident_id>/",
        views.subscribe_incident_view,
        name="subscribe_incident",
    ),
    path("seguir/area/", views.subscribe_area_view, name="subscribe_area"),
]
