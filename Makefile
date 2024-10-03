install:
	poetry install

test:
    poetry run pytest -v

test-coverage:
    poetry run pytest --cov=gendiff --cov-test-coverage xml

lint:
	poetry run flake8 gendiff

selfcheck:
    poetry check

check:
    selfcheck test lint

build: check
        poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*whl

package-install-force:
	python3 -m pip install --user --force-reinstall dist/*.whl

.PHONY: install test lint selfcheck check build

