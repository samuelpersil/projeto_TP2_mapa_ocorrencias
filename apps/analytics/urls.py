"""Roteamento de URLs da aplicação analytics."""

from django.urls import path

from apps.analytics import views

app_name = "analytics"

urlpatterns = [
    path("", views.analytics_dashboard_view, name="dashboard"),
    path("api/heatmap/", views.heatmap_data_api, name="heatmap_api"),
]
