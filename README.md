# python-open-restaurant-fastapi

Demo API using fastapi with one route that takes a datetime string and returns open restaurants, if any

## Table of Contents

- [python-open-restaurant-fastapi](#python-open-restaurant-fastapi)
  - [Table of Contents](#table-of-contents)
  - [Pre-requisites](#pre-requisites)
    - [.env File](#env-file)
    - [Docker](#docker)
    - [Alembic Database Migrations](#alembic-database-migrations)
  - [Linting](#linting)
  - [Testing](#testing)
  - [CSV Row Totals](#csv-row-totals)

## Pre-requisites

### .env File

Create a .env file in the root directory of your project based off of the `.env.sample` file.

### Docker

Install Docker and run the following command to startup the database/api in Docker:

```sh
docker compose up --build --pull postgresql --remove-orphans -V --wait
```

### Alembic Database Migrations

Once the database is up, we need to perform the database migration. To do this, run the following command:

```sh
poetry run alembic upgrade head
```

## Linting

To lint the project, run the following commands:

```shell
poetry run flake8 app tests
poetry run pylint app tests
```

## Testing

To run the tests, be sure you have ran the [Docker Compose Command](#docker) and the [Alembic Database Migrations](#alembic-database-migrations), then run the following command:

```sh
poetry run pytest --cov --cov-report=html -n auto
```

This will run the tests using xdist on multiple threads and generate a coverage report in the htmlcov directory.

## CSV Row Totals

I imported the provided CSV into Google Sheets to easily calculate the number of rows the csv import should make. You can view that via this link: [https://docs.google.com/spreadsheets/d/1t4kAuOgT4Oqoldq02rXDrrO2Mwgy80UkcfTBPhnlpK4/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1t4kAuOgT4Oqoldq02rXDrrO2Mwgy80UkcfTBPhnlpK4/edit?usp=sharing)
