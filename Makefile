install:
	poetry install

lint:
	flake8 .

test:
	poetry run pytest

check: lint test
