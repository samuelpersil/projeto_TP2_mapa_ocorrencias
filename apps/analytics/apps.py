"""Configuração da aplicação analytics."""

from django.apps import AppConfig


class AnalyticsConfig(AppConfig):
    """Configuração padrão do app de analytics."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.analytics"
    verbose_name = "Estatísticas e Mapas de Calor"
