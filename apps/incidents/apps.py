"""Configuração da aplicação incidents."""

from django.apps import AppConfig


class IncidentsConfig(AppConfig):
    """Configuração padrão do app de ocorrências."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.incidents"
    verbose_name = "Ocorrências Urbanas"
