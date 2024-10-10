install:
	poetry install

lint:
	poetry run flake8 .

test:
	poetry run pytest

check:
        lint test
