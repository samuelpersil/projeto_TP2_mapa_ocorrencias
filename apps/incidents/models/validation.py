"""Modelo de validação comunitária de ocorrências.

Responsável pelo Módulo 3: Luan Vinicius do Nascimento Alves.
"""

from django.db import models


class IncidentValidation(models.Model):
    """Voto de validação comunitária ('Ainda está lá' ou 'Já foi resolvido')."""

    # --------------------------------------------------------------------------
    # SPRINT 2 - PASSO 1 (Historieta 3): Modelo de Validação Comunitária
    # ORIENTAÇÃO TDD: Testar em tests/incidents/test_validation.py que um mesmo
    # usuário não pode registrar dois votos ativos na mesma ocorrência.
    # NOTAS DE IMPLEMENTAÇÃO: Usar ForeignKey para Incident e User, campo vote_type
    # (CONFIRM / RESOLVE) e UniqueConstraint(fields=['incident', 'user']).
    # --------------------------------------------------------------------------

    class Meta:
        verbose_name = "Validação Comunitária"
        verbose_name_plural = "Validações Comunitárias"

    def __str__(self) -> str:
        """Retorna resumo do voto de validação."""
        raise NotImplementedError("TODO: Implementar seguindo TDD")
