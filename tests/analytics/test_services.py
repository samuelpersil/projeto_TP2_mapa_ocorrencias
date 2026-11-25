"""Testes dos pipelines analíticos com Pandas e mapa de calor."""


def test_compute_incidents_by_category_and_region() -> None:
    """Valida agregação de ocorrências por categoria e região com Pandas."""
    # --------------------------------------------------------------------------
    # SPRINT 3 - PASSO 1 (Historieta 5): Teste de Agregação com Pandas
    # ORIENTAÇÃO TDD: Passar queryset/dados simulados e validar contagens por
    # categoria e tratamento seguro de conjunto vazio.
    # NOTAS DE IMPLEMENTAÇÃO: Testar compute_incidents_by_category_and_region().
    # --------------------------------------------------------------------------
    raise NotImplementedError("TODO: Implementar seguindo TDD")


def test_generate_heatmap_coordinates() -> None:
    """Valida geração de triplas [lat, lng, intensity] para Leaflet.heat."""
    # --------------------------------------------------------------------------
    # SPRINT 3 - PASSO 5 (Historieta 5): Teste de Coordenadas do Mapa de Calor
    # ORIENTAÇÃO TDD: Verificar que a saída é uma lista de listas [lat, lng, w]
    # com valores float válidos.
    # NOTAS DE IMPLEMENTAÇÃO: Testar generate_heatmap_coordinates().
    # --------------------------------------------------------------------------
    raise NotImplementedError("TODO: Implementar seguindo TDD")
