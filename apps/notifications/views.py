"""Views de caixa de entrada e inscrições de acompanhamento.

Responsável pelo Módulo 4: Renato Gabriel Lima da Silva.
"""

from django.http import HttpRequest, HttpResponse, JsonResponse


def inbox_view(request: HttpRequest) -> HttpResponse:
    """Exibe as notificações do usuário autenticado."""
    # --------------------------------------------------------------------------
    # SPRINT 2 - PASSO 8 (Historieta 4): Caixa de Entrada de Notificações
    # ORIENTAÇÃO TDD: Testar que usuário autenticado visualiza suas notificações
    # e usuário anônimo é redirecionado para login.
    # NOTAS DE IMPLEMENTAÇÃO: Filtrar Notification por request.user e marcar
    # como lidas quando solicitado.
    # --------------------------------------------------------------------------
    raise NotImplementedError("TODO: Implementar seguindo TDD")


def subscribe_incident_view(request: HttpRequest, incident_id: int) -> JsonResponse:
    """Inscreve ou desinscreve o usuário no acompanhamento de uma ocorrência."""
    # --------------------------------------------------------------------------
    # SPRINT 2 - PASSO 9 (Historieta 4): Seguir Ocorrência
    # ORIENTAÇÃO TDD: Testar toggle de inscrição via POST retornando JSON com
    # o estado atual (subscribed: True/False).
    # NOTAS DE IMPLEMENTAÇÃO: Usar get_or_create / delete em IncidentSubscription.
    # --------------------------------------------------------------------------
    raise NotImplementedError("TODO: Implementar seguindo TDD")


def subscribe_area_view(request: HttpRequest) -> JsonResponse:
    """Cria uma inscrição de monitoramento para um raio geográfico."""
    # --------------------------------------------------------------------------
    # SPRINT 2 - PASSO 10 (Historieta 4): Seguir Área Geográfica
    # ORIENTAÇÃO TDD: Testar POST com center_lat, center_lng, radius_km e label
    # válidos criando AreaSubscription para request.user.
    # NOTAS DE IMPLEMENTAÇÃO: Validar parâmetros numéricos antes de persistir.
    # --------------------------------------------------------------------------
    raise NotImplementedError("TODO: Implementar seguindo TDD")
