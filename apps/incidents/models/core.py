"""Modelos principais de ocorrências, categorias e configuração do sistema.

Responsável pelo Módulo 1: Giovanna Sperandio (Scrum Master).
"""

from django.db import models


class Category(models.Model):
    """Categoria de ocorrência urbana permitida no sistema."""

    # --------------------------------------------------------------------------
    # SPRINT 1 - PASSO 1 (Historieta 6): Modelo de Categorias de Ocorrência
    # ORIENTAÇÃO TDD: Escrever teste em tests/incidents/test_models.py validando
    # criação de categoria, unicidade do nome e representação __str__.
    # NOTAS DE IMPLEMENTAÇÃO: Adicionar campos name (CharField unique),
    # icon (CharField) e color (CharField) com valores padrão.
    # --------------------------------------------------------------------------

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self) -> str:
        """Retorna o nome legível da categoria."""
        raise NotImplementedError("TODO: Implementar seguindo TDD")


class SystemConfiguration(models.Model):
    """Configuração global singleton com bounding box GPS e limiares."""

    # --------------------------------------------------------------------------
    # SPRINT 1 - PASSO 2 (Historieta 6): Modelo Singleton de Parametrização
    # ORIENTAÇÃO TDD: Testar que apenas uma instância ativa pode existir e que
    # min_lat < max_lat e min_lng < max_lng são validados.
    # NOTAS DE IMPLEMENTAÇÃO: Campos min_lat, max_lat, min_lng, max_lng
    # (FloatField) e limiares de confirmação/resolução (PositiveIntegerField).
    # --------------------------------------------------------------------------

    class Meta:
        verbose_name = "Configuração do Sistema"
        verbose_name_plural = "Configurações do Sistema"

    def __str__(self) -> str:
        """Retorna descrição da configuração ativa."""
        raise NotImplementedError("TODO: Implementar seguindo TDD")


class Incident(models.Model):
    """Registro de ocorrência urbana geolocalizada."""

    # --------------------------------------------------------------------------
    # SPRINT 1 - PASSO 3 (Historieta 1): Modelo Principal de Ocorrência
    # ORIENTAÇÃO TDD: Testar criação com category FK, latitude, longitude,
    # photo opcional (ImageField), description, status e reporter FK.
    # NOTAS DE IMPLEMENTAÇÃO: Usar TextChoices para status (ABERTA, CONFIRMADA,
    # RESOLVIDA), auto_now_add=True em created_at e validar coordenadas GPS.
    # --------------------------------------------------------------------------

    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"

    def __str__(self) -> str:
        """Retorna resumo da ocorrência."""
        raise NotImplementedError("TODO: Implementar seguindo TDD")
