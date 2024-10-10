#!/bin/bash
poetry run flake8 app tests
poetry run pylint app tests

docker compose up --build --pull always --remove-orphans -V --wait
poetry run alembic upgrade head
poetry run pytest --cov --cov-report=html -n auto
