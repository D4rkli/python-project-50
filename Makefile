.PHONY: test lint coverage check

install:
	uv sync
	uv pip install --system

setup:
	uv venv
	uv pip sync pyproject.toml
run:
	uv run hexlet-python-package

test:
	uv run pytest

package-install:
	uv tool install

lint:
	uv pip install flake8
	flake8 gendiff tests\

coverage:
	uv pip install pytest pytest-cov
	pytest --cov=gendiff --cov-report=xml

check: lint test coverage
