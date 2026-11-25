"""Views do painel de estatísticas e API do mapa de calor.

Responsável pelo Módulo 5: Samuel Pereira da Silveira (Product Owner).
"""

from django.http import HttpRequest, HttpResponse, JsonResponse


def analytics_dashboard_view(request: HttpRequest) -> HttpResponse:
    """Renderiza o painel administrativo de estatísticas com Pandas."""
    # --------------------------------------------------------------------------
    # SPRINT 3 - PASSO 6 (Historieta 5): Painel de Estatísticas
    # ORIENTAÇÃO TDD: Testar que GET /analytics/ retorna status 200 (ou 403/302
    # para não-administradores) e renderiza analytics/dashboard.html.
    # NOTAS DE IMPLEMENTAÇÃO: Chamar funções de apps/analytics/services.py e
    # enviar métricas agregadas para o template.
    # --------------------------------------------------------------------------
    raise NotImplementedError("TODO: Implementar seguindo TDD")


def heatmap_data_api(request: HttpRequest) -> JsonResponse:
    """Retorna coordenadas [lat, lng, intensity] em JSON para o Leaflet.heat."""
    # --------------------------------------------------------------------------
    # SPRINT 3 - PASSO 7 (Historieta 5): Endpoint JSON do Mapa de Calor
    # ORIENTAÇÃO TDD: Testar retorno JSON com chave 'points' contendo lista de
    # triplas numéricas [lat, lng, intensity].
    # NOTAS DE IMPLEMENTAÇÃO: Filtrar ocorrências por período/categoria opcionais
    # e delegar a generate_heatmap_coordinates().
    # --------------------------------------------------------------------------
    raise NotImplementedError("TODO: Implementar seguindo TDD")
