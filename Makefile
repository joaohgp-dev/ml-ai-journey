# Makefile - Tarefas utilitárias para desenvolvimento

.PHONY: help install lint test format clean

## Mostra esta ajuda
help:
	@echo ""
	@echo "Comandos disponíveis:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'
	@echo ""

## Instala dependências do projeto
install:
	pip install -r requirements.txt

## Executa linter com flake8
lint:
	flake8 .

## Executa os testes com pytest
test:
	pytest

## Formata o código com black
format:
	black .

## Remove arquivos temporários e caches
clean:
	find . -type d -name '__pycache__' -exec rm -r {} + || true
	find . -type f -name '*.pyc' -delete || true
