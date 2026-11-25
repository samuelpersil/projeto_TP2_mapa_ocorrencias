# Gestão Urbana — Sistema de Ocorrências GPS

Projeto submetido como trabalho final da disciplina **Técnicas de Programação 2 (2/2026)** — Universidade de Brasília (UnB).  
**Entrega final:** 30 de novembro de 2026.

## 1. Visão Geral do Projeto

O **Gestão Urbana** é uma aplicação web *mobile-first* para registro, visualização em mapa comunitário, validação colaborativa, acompanhamento por notificações e análise estatística (com mapas de calor) de ocorrências urbanas geolocalizadas.

## 2. Stack Tecnológica e Licenças Open Source

| Tecnologia | Finalidade | Licença |
| :--- | :--- | :--- |
| **Python 3.12+ / Django** | Backend, ORM, Admin e Templates | BSD-3-Clause |
| **SQLite** | Banco de dados local de desenvolvimento | Domínio Público |
| **Bootstrap 5** | Interface responsiva *mobile-first* | MIT |
| **Leaflet.js + Leaflet.heat** | Mapa interativo e mapa de calor | BSD-2-Clause |
| **OpenStreetMap** | Camada de tiles cartográficos | ODbL |
| **Pandas** | Agregações estatísticas e séries temporais | BSD-3-Clause |
| **Pytest + Coverage.py** | Testes automatizados e cobertura | MIT / Apache-2.0 |
| **Ruff + Pylint** | Linting e conformidade PEP 8 | MIT / GPL-2.0 |
| **MkDocs + Material** | Documentação técnica automatizada | MIT / BSD |

## 3. Guia Rápido de Instalação e Execução (`Makefile`)

```bash
# 0. Verificar todos os comandos disponíveis
make help

# 1. Instalar dependências
make install

# 2. Gerar e aplicar migrações do banco SQLite
make migrate

# 3. Criar superusuário administrador (opcional)
make superuser

# 4. Iniciar servidor de desenvolvimento
make run
```

Outros comandos úteis:
- `make lint` — executa `ruff check .` e `pylint --load-plugins=pylint_django apps config`.
- `make format` — formata o código com `ruff format .` e corrige imports.
- `make docs-serve` — inicia a documentação local com MkDocs.
- `make clean` — remove caches e artefatos temporários.

## 4. Fluxo de TDD (Red-Green-Refactor) e Meta de Cobertura (>= 80%)

Todo desenvolvimento de domínio deve seguir estritamente o ciclo **Red → Green → Refactor**:
1. **Red:** Escrever o teste primeiro em `tests/` e confirmar que ele falha.
2. **Green:** Implementar o código mínimo em `apps/` para o teste passar.
3. **Refactor:** Melhorar a legibilidade e remover duplicações mantendo os testes verdes.

Para executar a suíte de testes com verificação de cobertura:

```bash
make test
```

> **Nota sobre o gate de 80%:** Na fase inicial de *scaffolding*, os corpos de domínio e testes contêm `NotImplementedError("TODO: Implementar seguindo TDD")`. O gate `--cov-fail-under=80` (configurado no `Makefile` e comentado no `.github/workflows/ci.yml`) passa a valer assim que os *stubs* da Sprint 1 forem implementados.

## 5. Regras de Linting e Qualidade (Ruff + Pylint + SonarLint)

- Padrão **PEP 8** com limite de 88 caracteres por linha (`pyproject.toml`).
- **Type hints** obrigatórios em funções, métodos e testes.
- Docstrings e comentários em **Português do Brasil (pt-BR)**.
- Recomenda-se habilitar a extensão **SonarLint** na IDE para inspeção contínua de *code smells*.

## 6. Quadro Kanban / Backlog Inicial (GitHub Projects)

| Módulo | Responsável | Historieta(s) | Arquivos Principais (Sem Conflito) | Status Inicial |
| :--- | :--- | :--- | :--- | :--- |
| **Módulo 1 — Core, Admin e Registro** | **Giovanna Sperandio David** *(Scrum Master)* | Historieta 1 e 6 | `apps/incidents/models/core.py`, `forms.py`, `admin.py` | `To Do` |
| **Módulo 2 — Mapa Comunitário e Views** | **Leonardo Aoki Sachi** | Historieta 1 e 2 | `apps/incidents/views/map_views.py`, `templates/incidents/*.html`, `static/js/map.js` | `To Do` |
| **Módulo 3 — Validação Comunitária** | **Luan Vinicius do Nascimento Alves** | Historieta 3 | `apps/incidents/models/validation.py`, `apps/incidents/views/validation_views.py` | `To Do` |
| **Módulo 4 — Acompanhamento e Notificações** | **Renato Gabriel Lima da Silva** | Historieta 4 | `apps/notifications/models.py`, `services.py`, `views.py`, `admin.py` | `To Do` |
| **Módulo 5 — Analytics e Mapa de Calor** | **Samuel Pereira da Silveira** *(Product Owner)* | Historieta 5 | `apps/analytics/services.py`, `views.py`, `templates/analytics/dashboard.html` | `To Do` |
