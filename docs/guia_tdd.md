# Guia de TDD (Red-Green-Refactor)

Todos os módulos possuem *stubs* com blocos de orientação TDD em português:

1. **Red:** Abra o arquivo correspondente em `tests/`, implemente o teste e rode `pytest` para confirmar a falha esperada.
2. **Green:** Implemente a lógica mínima em `apps/` até o teste passar.
3. **Refactor:** Refatore mantendo `make lint` e `make test` verdes (cobertura mínima de 80%).
