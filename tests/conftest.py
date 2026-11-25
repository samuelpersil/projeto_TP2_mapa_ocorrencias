"""Fixtures compartilhadas do Pytest para os testes do Gestão Urbana."""

from typing import Any

import pytest
from django.test import Client


@pytest.fixture
def client() -> Client:
    """Retorna um cliente HTTP de testes do Django."""
    return Client()


@pytest.fixture
def sample_user_data() -> dict[str, Any]:
    """Retorna dados de exemplo para criação de usuário em testes."""
    return {
        "username": "cidadao_unb",
        "email": "cidadao@unb.br",
        "password": "senha_segura_tp2_2026",
    }
