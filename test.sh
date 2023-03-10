#!/bin/bash
docker compose up --build --pull postgresql --remove-orphans -V --wait
alembic upgrade head
pytest --cov --cov-report=html -n auto
