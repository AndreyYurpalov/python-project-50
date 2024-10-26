install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

lint:
	poetry run flake8

check: test lint

build: check
	poetry build

.PHONY: install test lint selfcheck check build
