"""Roteamento de URLs da aplicação incidents."""

from django.urls import path

from apps.incidents.views import map_views, validation_views

app_name = "incidents"

urlpatterns = [
    path("", map_views.map_view, name="map"),
    path("api/incidents/", map_views.incidents_geojson_api, name="incidents_api"),
    path("novo/", map_views.create_incident_view, name="create_incident"),
    path(
        "<int:incident_id>/confirmar/",
        validation_views.confirm_incident_view,
        name="confirm_incident",
    ),
    path(
        "<int:incident_id>/resolver/",
        validation_views.resolve_incident_view,
        name="resolve_incident",
    ),
]
