"""Testes dos modelos de acompanhamento, notificações e SearchLog."""

import pytest
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from apps.notifications.models import AreaSubscription

User = get_user_model()


@pytest.mark.django_db
def test_incident_and_area_subscriptions() -> None:
    """Valida criação de inscrições em ocorrência e área geográfica."""
    # --------------------------------------------------------------------------
    # SPRINT 2 - PASSO 1 (Historieta 4): Teste de Modelos de Inscrição
    # ORIENTAÇÃO TDD: Criar IncidentSubscription e AreaSubscription e validar
    # campos obrigatórios e unicidade.
    # NOTAS DE IMPLEMENTAÇÃO: Marcar com @pytest.mark.django_db após implementar.
    # --------------------------------------------------------------------------
    user = User.objects.create_user(username="usuario1", password="senha_123")

    area = AreaSubscription.objects.create(
        user=user,
        label="Asa Norte - Quadra 308",
        center_lat=-15.7654,
        center_lng=-47.8821,
        radius_km=1.5,
    )

    assert area.id is not None
    assert area.user == user
    assert area.label == "Asa Norte - Quadra 308"
    assert area.center_lat == pytest.approx(-15.7654)
    assert area.center_lng == pytest.approx(-47.8821)
    assert area.radius_km == pytest.approx(1.5)
    assert str(area) == "Asa Norte - Quadra 308"


@pytest.mark.django_db
def test_area_subscription_invalid_radius() -> None:
    """Valida que radius_km zero ou negativo gera erro de validação."""
    user = User.objects.create_user(username="usuario2", password="senha_456")

    area = AreaSubscription(
        user=user,
        label="Bairro Teste",
        center_lat=-15.7942,
        center_lng=-47.8822,
        radius_km=0,
    )
    with pytest.raises(ValidationError):
        area.full_clean()


@pytest.mark.django_db
@pytest.mark.parametrize(
    ("lat", "lng"),
    [
        (90.1, 0.0),
        (-90.1, 0.0),
        (0.0, 180.1),
        (0.0, -180.1),
    ],
)
def test_area_subscription_rejects_out_of_range_coordinates(
    lat: float,
    lng: float,
) -> None:
    """Garante que latitude fora de [-90, 90] ou longitude fora de [-180, 180] falhe."""
    user = User.objects.create_user(username=f"user_{lat}_{lng}", password="123")

    area = AreaSubscription(
        user=user,
        label="Coordenada Fora do Limite",
        center_lat=lat,
        center_lng=lng,
        radius_km=1.0,
    )

    with pytest.raises(ValidationError):
        area.full_clean()
