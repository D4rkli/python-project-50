.PHONY: test lint coverage check

install:
	uv sync
	uv pip install --system

setup:
	uv venv
	uv pip sync pyproject.toml
	uv pip install flake8 coverage
run:
	uv run hexlet-python-package

test:
	uv run pytest

package-install:
	uv tool install

lint:
	uv run flake8 gendiff tests

coverage:
	uv run coverage run -m pytest
	uv run coverage report

check: lint test coverage
