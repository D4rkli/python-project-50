.PHONY: install lint test

install:
	poetry install

lint:
	poetry run flake8 .

test:
	poetry run pytest
