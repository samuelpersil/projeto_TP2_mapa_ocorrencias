"""Serviços de disparo de notificações e registro de buscas.

Responsável pelo Módulo 4: Renato Gabriel Lima da Silva.
"""

from typing import Any


def notify_incident_status_change(incident: Any, new_status: str) -> int:
    """Cria notificações para todos os inscritos quando o status muda."""
    # --------------------------------------------------------------------------
    # SPRINT 2 - PASSO 5 (Historieta 4): Disparo por Mudança de Status
    # ORIENTAÇÃO TDD: Testar em tests/notifications/test_services.py que todos
    # os usuários inscritos recebem exatamente uma Notification ao mudar status.
    # NOTAS DE IMPLEMENTAÇÃO: Consultar IncidentSubscription e usar bulk_create
    # em Notification para eficiência. Retornar quantidade criada.
    # --------------------------------------------------------------------------
    raise NotImplementedError("TODO: Implementar seguindo TDD")


def notify_area_subscribers(incident: Any) -> int:
    """Notifica usuários que monitoram a área onde a ocorrência foi criada."""
    # --------------------------------------------------------------------------
    # SPRINT 2 - PASSO 6 (Historieta 4): Disparo por Proximidade Geográfica
    # ORIENTAÇÃO TDD: Testar cálculo de distância (Haversine) entre incident e
    # AreaSubscription, notificando apenas inscritos dentro de radius_km.
    # NOTAS DE IMPLEMENTAÇÃO: Implementar helper puro de distância Haversine em
    # quilômetros e criar Notification para os usuários elegíveis.
    # --------------------------------------------------------------------------
    raise NotImplementedError("TODO: Implementar seguindo TDD")


def log_search_query(
    user: Any,
    query_text: str,
    category_name: str = "",
) -> None:
    """Registra uma consulta realizada no mapa na tabela SearchLog."""
    # --------------------------------------------------------------------------
    # SPRINT 2 - PASSO 7 (Historieta 4 e 5): Helper de Log de Buscas
    # ORIENTAÇÃO TDD: Testar que chamadas válidas persistem um SearchLog no
    # banco e ignoram consultas vazias sem lançar exceção.
    # NOTAS DE IMPLEMENTAÇÃO: Normalizar query_text (strip/lower) antes de
    # salvar em SearchLog.objects.create(...).
    # --------------------------------------------------------------------------
    raise NotImplementedError("TODO: Implementar seguindo TDD")
