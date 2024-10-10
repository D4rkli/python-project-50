install:
	poetry install

lint:
	poetry run flake8 hexlet_code

test:
	poetry run pytest

check: lint test
