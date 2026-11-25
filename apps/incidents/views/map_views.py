"""Views do mapa comunitário e cadastro de ocorrências.

Responsável pelo Módulo 2: Leonardo Aoki Sachi.
"""

from django.http import HttpRequest, HttpResponse, JsonResponse


def map_view(request: HttpRequest) -> HttpResponse:
    """Renderiza a página principal com o mapa interativo Leaflet.js."""
    # --------------------------------------------------------------------------
    # SPRINT 1 - PASSO 1 (Historieta 2): View Principal do Mapa Comunitário
    # ORIENTAÇÃO TDD: Testar em tests/incidents/test_views.py que GET / retorna
    # status 200 e utiliza o template incidents/map.html.
    # NOTAS DE IMPLEMENTAÇÃO: Usar django.shortcuts.render com contexto inicial
    # de categorias para filtros no mapa.
    # --------------------------------------------------------------------------
    raise NotImplementedError("TODO: Implementar seguindo TDD")


def incidents_geojson_api(request: HttpRequest) -> JsonResponse:
    """Retorna ocorrências em formato JSON/GeoJSON filtradas por bounding box."""
    # --------------------------------------------------------------------------
    # SPRINT 1 - PASSO 2 (Historieta 2): Endpoint JSON de Ocorrências no Mapa
    # ORIENTAÇÃO TDD: Testar filtragem por parâmetros min_lat, max_lat, min_lng,
    # max_lng e estrutura GeoJSON retornada para o Leaflet.js.
    # NOTAS DE IMPLEMENTAÇÃO: Filtrar Incident via Django ORM e registrar a busca
    # utilizando o helper de SearchLog do módulo de notificações.
    # --------------------------------------------------------------------------
    raise NotImplementedError("TODO: Implementar seguindo TDD")


def create_incident_view(request: HttpRequest) -> HttpResponse:
    """Exibe e processa o formulário de registro de nova ocorrência."""
    # --------------------------------------------------------------------------
    # SPRINT 1 - PASSO 3 (Historieta 1): View de Criação de Ocorrência
    # ORIENTAÇÃO TDD: Testar GET /novo/ (status 200) e POST válido criando
    # registro no banco e redirecionando para o mapa.
    # NOTAS DE IMPLEMENTAÇÃO: Validar IncidentForm (incluindo request.FILES) e
    # associar request.user como reporter quando autenticado.
    # --------------------------------------------------------------------------
    raise NotImplementedError("TODO: Implementar seguindo TDD")
