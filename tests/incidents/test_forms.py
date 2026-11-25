"""Testes unitários para IncidentForm."""


def test_incident_form_valid_coordinates() -> None:
    """Valida que coordenadas dentro do bounding box são aceitas."""
    # --------------------------------------------------------------------------
    # SPRINT 1 - PASSO 4 (Historieta 1): Teste de Validação Geo do Formulário
    # ORIENTAÇÃO TDD: Submeter dados válidos ao IncidentForm e checar is_valid().
    # NOTAS DE IMPLEMENTAÇÃO: Configurar SystemConfiguration com limites de DF.
    # --------------------------------------------------------------------------
    raise NotImplementedError("TODO: Implementar seguindo TDD")


def test_incident_form_out_of_bounds_coordinates() -> None:
    """Valida que coordenadas fora do bounding box são rejeitadas."""
    # --------------------------------------------------------------------------
    # SPRINT 1 - PASSO 4 (Historieta 1): Teste de Rejeição Geo no Formulário
    # ORIENTAÇÃO TDD: Submeter latitude/longitude fora dos limites e verificar
    # que form.is_valid() retorna False com erro claro.
    # NOTAS DE IMPLEMENTAÇÃO: Verificar presença de mensagem em form.errors.
    # --------------------------------------------------------------------------
    raise NotImplementedError("TODO: Implementar seguindo TDD")
