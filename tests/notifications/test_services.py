"""Testes dos serviços de notificação e registro de buscas."""


def test_notify_incident_status_change() -> None:
    """Valida envio de notificação aos inscritos quando o status muda."""
    # --------------------------------------------------------------------------
    # SPRINT 2 - PASSO 5 (Historieta 4): Teste de Disparo de Notificações
    # ORIENTAÇÃO TDD: Chamar notify_incident_status_change e verificar que o
    # número de Notification criadas corresponde aos inscritos.
    # NOTAS DE IMPLEMENTAÇÃO: Validar conteúdo da mensagem e is_read=False.
    # --------------------------------------------------------------------------
    raise NotImplementedError("TODO: Implementar seguindo TDD")


def test_log_search_query() -> None:
    """Valida persistência de consultas no SearchLog."""
    # --------------------------------------------------------------------------
    # SPRINT 2 - PASSO 7 (Historieta 4 e 5): Teste de Log de Buscas
    # ORIENTAÇÃO TDD: Chamar log_search_query com termo válido e vazio,
    # verificando que apenas o termo válido é salvo em SearchLog.
    # NOTAS DE IMPLEMENTAÇÃO: Checar normalização (strip/lower).
    # --------------------------------------------------------------------------
    raise NotImplementedError("TODO: Implementar seguindo TDD")
