"""Configuração da aplicação notifications."""

from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    """Configuração padrão do app de notificações."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.notifications"
    verbose_name = "Notificações e Acompanhamento"
