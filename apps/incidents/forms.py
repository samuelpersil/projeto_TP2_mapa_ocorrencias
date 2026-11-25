"""Formulários do app incidents.

Responsável pelo Módulo 1: Giovanna Sperandio (Scrum Master).
"""

from typing import Any

from django import forms


class IncidentForm(forms.Form):
    """Formulário mobile-first para registro de ocorrências com GPS."""

    # --------------------------------------------------------------------------
    # SPRINT 1 - PASSO 4 (Historieta 1): Formulário de Registro de Ocorrência
    # ORIENTAÇÃO TDD: Testar em tests/incidents/test_forms.py a validação de
    # coordenadas fora do bounding box de SystemConfiguration e foto opcional.
    # NOTAS DE IMPLEMENTAÇÃO: Converter para ModelForm de Incident quando o
    # modelo estiver implementado, adicionando validação geo no método clean().
    # --------------------------------------------------------------------------

    def clean(self) -> dict[str, Any]:
        """Valida coordenadas geográficas contra a configuração do sistema."""
        raise NotImplementedError("TODO: Implementar seguindo TDD")
