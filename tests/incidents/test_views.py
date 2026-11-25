"""Testes de integração para as views do mapa e cadastro de ocorrências."""

from django.test import Client


def test_map_view_status_200(client: Client) -> None:
    """Valida que a página principal do mapa responde com HTTP 200."""
    # --------------------------------------------------------------------------
    # SPRINT 1 - PASSO 1 (Historieta 2): Teste da View do Mapa
    # ORIENTAÇÃO TDD: Fazer GET / via client e verificar status_code == 200.
    # NOTAS DE IMPLEMENTAÇÃO: Verificar também o template incidents/map.html.
    # --------------------------------------------------------------------------
    raise NotImplementedError("TODO: Implementar seguindo TDD")


def test_incidents_geojson_api(client: Client) -> None:
    """Valida o endpoint JSON de ocorrências filtradas por bounding box."""
    # --------------------------------------------------------------------------
    # SPRINT 1 - PASSO 2 (Historieta 2): Teste da API GeoJSON do Mapa
    # ORIENTAÇÃO TDD: Fazer GET /api/incidents/ com parâmetros de bounding box
    # e validar que apenas ocorrências dentro da área são retornadas.
    # NOTAS DE IMPLEMENTAÇÃO: Checar response.json() e estrutura GeoJSON.
    # --------------------------------------------------------------------------
    raise NotImplementedError("TODO: Implementar seguindo TDD")
