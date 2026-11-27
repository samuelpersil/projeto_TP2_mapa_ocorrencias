"""Modelos de acompanhamento, notificações e registro de buscas.

Responsável pelo Módulo 4: Renato Gabriel Lima da Silva.
"""
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


class IncidentSubscription(models.Model):
    """Inscrição de um usuário para acompanhar uma ocorrência específica."""

    # --------------------------------------------------------------------------
    # SPRINT 2 - PASSO 1 (Historieta 4): Inscrição em Ocorrência
    # ORIENTAÇÃO TDD: Testar em tests/notifications/test_models.py que um usuário
    # pode seguir uma ocorrência sem duplicidade (UniqueConstraint).
    # NOTAS DE IMPLEMENTAÇÃO: ForeignKey para User e apps.incidents.Incident.
    # --------------------------------------------------------------------------

    class Meta:
        verbose_name = "Inscrição em Ocorrência"
        verbose_name_plural = "Inscrições em Ocorrências"

    def __str__(self) -> str:
        """Retorna descrição da inscrição."""
        raise NotImplementedError("TODO: Implementar seguindo TDD")


class AreaSubscription(models.Model):
    """Inscrição de um usuário para monitorar um raio geográfico/bairro."""

    # --------------------------------------------------------------------------
    # SPRINT 2 - PASSO 2 (Historieta 4): Monitoramento de Área Geográfica
    # ORIENTAÇÃO TDD: Testar criação de área com center_lat, center_lng e
    # radius_km positivos.
    # NOTAS DE IMPLEMENTAÇÃO: Campos user (FK), label (CharField), center_lat,
    # center_lng (FloatField) e radius_km (FloatField).
    # --------------------------------------------------------------------------

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="area_subscriptions",
    )
    label = models.CharField(max_length=120)
    center_lat = models.FloatField()
    center_lng = models.FloatField()
    radius_km = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Inscrição em Área"
        verbose_name_plural = "Inscrições em Áreas"
        ordering = ["-created_at"]

    def clean(self) -> None:
        super().clean()
        errors: dict[str, str] = {}

        if self.radius_km is not None and self.radius_km <= 0:
            errors["radius_km"] = "O raio deve ser maior que zero."

        if self.center_lat is not None and not (-90.0 <= self.center_lat <= 90.0):
            errors["center_lat"] = "A latitude deve estar entre -90 e 90."

        if self.center_lng is not None and not (-180.0 <= self.center_lng <= 180.0):
            errors["center_lng"] = "A longitude deve estar entre -180 e 180."

        if errors:
            raise ValidationError(errors)

    def __str__(self) -> str:
        """Retorna o rótulo da área monitorada."""
        return self.label


class Notification(models.Model):
    """Notificação entregue na caixa de entrada do usuário."""

    # --------------------------------------------------------------------------
    # SPRINT 2 - PASSO 3 (Historieta 4): Caixa de Entrada de Notificações
    # ORIENTAÇÃO TDD: Testar criação de notificação não lida (is_read=False)
    # associada a um usuário e ordenação por created_at decrescente.
    # NOTAS DE IMPLEMENTAÇÃO: Campos user (FK), incident (FK opcional), message
    # (TextField), is_read (BooleanField) e created_at (DateTimeField).
    # --------------------------------------------------------------------------

    class Meta:
        verbose_name = "Notificação"
        verbose_name_plural = "Notificações"

    def __str__(self) -> str:
        """Retorna resumo da notificação."""
        raise NotImplementedError("TODO: Implementar seguindo TDD")


class SearchLog(models.Model):
    """Registro de consultas e filtros realizados no mapa pelos usuários."""

    # --------------------------------------------------------------------------
    # SPRINT 2 - PASSO 4 (Historieta 4 e 5): Log de Buscas para Analytics
    # ORIENTAÇÃO TDD: Testar gravação de query_text, category_filter e
    # timestamp para consumo pelo módulo de analytics com Pandas.
    # NOTAS DE IMPLEMENTAÇÃO: Campos user (FK nullable), query_text (CharField),
    # category_name (CharField) e created_at (DateTimeField auto_now_add=True).
    # --------------------------------------------------------------------------

    class Meta:
        verbose_name = "Registro de Busca"
        verbose_name_plural = "Registros de Busca"

    def __str__(self) -> str:
        """Retorna resumo da busca registrada."""
        raise NotImplementedError("TODO: Implementar seguindo TDD")
