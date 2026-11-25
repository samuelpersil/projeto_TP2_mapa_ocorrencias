"""Views AJAX/JSON de validação comunitária de ocorrências.

Responsável pelo Módulo 3: Luan Vinicius do Nascimento Alves.
"""

from django.http import HttpRequest, JsonResponse


def confirm_incident_view(request: HttpRequest, incident_id: int) -> JsonResponse:
    """Registra voto 'Ainda está lá' e atualiza status se atingir o limiar."""
    # --------------------------------------------------------------------------
    # SPRINT 2 - PASSO 2 (Historieta 3): Endpoint 'Ainda está lá'
    # ORIENTAÇÃO TDD: Testar POST autenticado incrementando confirmações e
    # bloqueando voto duplicado do mesmo usuário; verificar transição de status.
    # NOTAS DE IMPLEMENTAÇÃO: Usar transaction.atomic() e consultar o limiar
    # global em SystemConfiguration antes de alterar o status do Incident.
    # --------------------------------------------------------------------------
    raise NotImplementedError("TODO: Implementar seguindo TDD")


def resolve_incident_view(request: HttpRequest, incident_id: int) -> JsonResponse:
    """Registra voto 'Já foi resolvido' e atualiza status se atingir o limiar."""
    # --------------------------------------------------------------------------
    # SPRINT 2 - PASSO 3 (Historieta 3): Endpoint 'Já foi resolvido'
    # ORIENTAÇÃO TDD: Testar POST autenticado registrando resolução e transição
    # automática do status para RESOLVIDA ao atingir o limiar configurado.
    # NOTAS DE IMPLEMENTAÇÃO: Reutilizar lógica compartilhada de validação e
    # disparar notificação de mudança de status para inscritos.
    # --------------------------------------------------------------------------
    raise NotImplementedError("TODO: Implementar seguindo TDD")
