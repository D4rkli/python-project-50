.PHONY: test lint coverage check

setup:
	uv venv
	uv pip install --upgrade pip
	uv pip install -r requirements.txt

test:
	uv pip install pytest
	pytest

lint:
	uv pip install flake8
	flake8 gendiff tests

coverage:
	uv pip install pytest pytest-cov
	pytest --cov=gendiff --cov-report=xml

check: lint test coverage
