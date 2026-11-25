PYTHON := $(if $(wildcard .venv/bin/python),.venv/bin/python,python3)
PIP := $(if $(wildcard .venv/bin/pip),.venv/bin/pip,pip)
PYTEST := $(if $(wildcard .venv/bin/pytest),.venv/bin/pytest,pytest)
RUFF := $(if $(wildcard .venv/bin/ruff),.venv/bin/ruff,ruff)
PYLINT := $(if $(wildcard .venv/bin/pylint),.venv/bin/pylint,pylint)
MKDOCS := $(if $(wildcard .venv/bin/mkdocs),.venv/bin/mkdocs,mkdocs)

.PHONY: help install migrate superuser run lint format test cov-html docs-build docs-serve clean

help:
	@echo "============================================================================"
	@echo " ⋆⁺₊✧⋆⁺₊✧⋆₊✧ PROJETO DE TP2 2026.2 - AUTOMATIZAÇÃO MAKEFILE ✧₊⁺⋆✧₊⁺⋆✧₊⁺⋆"
	@echo "============================================================================"
	@echo "✧ make install	  - Instala as dependências do projeto"
	@echo "✧ make lint	  - Executa verificação estática de código (Ruff e Pylint)"
	@echo "✧ make format	  - Formatar código automaticamente com Ruff"
	@echo "✧ make migrate	  - Executa makemigrations e migrate do Django"
	@echo "✧ make superuser  - Criar superusuário administrador (opcional)"
	@echo "✧ make test	  - Executa os testes automatizados com Pytest"
	@echo "✧ make run	  - Inicia o servidor de desenvolvimento (0.0.0.0:8000)"
	@echo "✧ make cov-html	  - Gera relatório de cobertura em HTML"
	@echo "✧ make docs-build - Constrói o servidor local de documentação com MkDocs"
	@echo "✧ make docs-serve - Inicia o servidor local de documentação com MkDocs"
	@echo "✧ make clean	  - Limpa arquivos temporários, caches e relatórios"
	@echo "============================================================================"
	@echo "⋆⁺₊✧⋆⁺₊✧⋆₊✧⋆⁺₊✧⋆⁺₊✧⋆₊✧⋆⁺₊✧⋆⁺₊✧⋆₊✧⋆⁺₊✧⋆⁺₊✧⋆₊✧⋆⁺₊✧⋆⁺₊✧⋆₊✧⋆⁺₊✧⋆⁺₊✧⋆₊✧⋆⁺₊"
	@echo "============================================================================"

install:
	$(PIP) install -r requirements.txt

migrate:
	$(PYTHON) manage.py makemigrations
	$(PYTHON) manage.py migrate

superuser:
	$(PYTHON) manage.py createsuperuser

run:
	$(PYTHON) manage.py runserver

lint:
	$(RUFF) check .
	$(PYLINT) --load-plugins=pylint_django apps config

format:
	$(RUFF) format .
	$(RUFF) check --fix .

test:
	$(PYTEST) --cov=apps --cov-report=term-missing --cov-fail-under=80

cov-html:
	$(PYTEST) --cov=apps --cov-report=html

docs-build:
	$(MKDOCS) build --strict

docs-serve:
	$(MKDOCS) serve

clean:
	rm -rf __pycache__ .pytest_cache .coverage htmlcov site
	find . -type d -name "__pycache__" -exec rm -rf {} +
