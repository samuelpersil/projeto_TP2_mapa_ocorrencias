"""Testes unitários para os modelos Category, SystemConfiguration e Incident."""


def test_create_category() -> None:
    """Valida a criação de uma categoria de ocorrência."""
    # --------------------------------------------------------------------------
    # SPRINT 1 - PASSO 1 (Historieta 6): Teste de Criação de Categoria
    # ORIENTAÇÃO TDD: Criar Category no banco, verificar __str__ e unicidade.
    # NOTAS DE IMPLEMENTAÇÃO: Marcar com @pytest.mark.django_db após implementar.
    # --------------------------------------------------------------------------
    raise NotImplementedError("TODO: Implementar seguindo TDD")


def test_system_configuration_singleton() -> None:
    """Valida que SystemConfiguration mantém apenas uma instância ativa."""
    # --------------------------------------------------------------------------
    # SPRINT 1 - PASSO 2 (Historieta 6): Teste de Singleton de Configuração
    # ORIENTAÇÃO TDD: Garantir que bounding box GPS inválido lance ValidationError.
    # NOTAS DE IMPLEMENTAÇÃO: Usar pytest.raises(ValidationError).
    # --------------------------------------------------------------------------
    raise NotImplementedError("TODO: Implementar seguindo TDD")


def test_create_incident() -> None:
    """Valida a criação de uma ocorrência com coordenadas GPS válidas."""
    # --------------------------------------------------------------------------
    # SPRINT 1 - PASSO 3 (Historieta 1): Teste de Criação de Ocorrência
    # ORIENTAÇÃO TDD: Criar Category e Incident e validar status inicial ABERTA.
    # NOTAS DE IMPLEMENTAÇÃO: Testar também criação sem foto (campo opcional).
    # --------------------------------------------------------------------------
    raise NotImplementedError("TODO: Implementar seguindo TDD")
