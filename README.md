# python-open-restaurant-fastapi

Demo API using fastapi with one route that takes a datetime string and returns open restaurants, if any

## Table of Contents

- [python-open-restaurant-fastapi](#python-open-restaurant-fastapi)
  - [Table of Contents](#table-of-contents)
  - [Pre-requisites](#pre-requisites)
    - [.env File](#env-file)
    - [Docker](#docker)
    - [Alembic Database Migrations](#alembic-database-migrations)
  - [Testing](#testing)
  - [CSV Row Totals](#csv-row-totals)

## Pre-requisites

### .env File

Create a .env file in the root directory with the following variables:

```sh
DATABASE_USER=postgres
DATABASE_PASSWORD=123456
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=postgres
```

### Docker

Install Docker and run the following command to startup the database/api in Docker:

```sh
docker compose up --build --pull postgresql --remove-orphans -V --wait
```

### Alembic Database Migrations

Once the database is up, we need to perform the database migration. To do this, run the following command:

```sh
alembic upgrade head
```

## Testing

To run the tests, be sure you have ran the [Docker Compose Command](#docker) and the [Alembic Database Migrations](#alembic-database-migrations) and then run the following command:

```sh
pytest --cov --cov-report=html -n auto
```

This will run the tests using xdist on multiple threads and generate a coverage report in the htmlcov directory.

## CSV Row Totals

I imported the provided CSV into Google Sheets to easily calculate the number of rows the csv import should make. You can view that via this link: [https://docs.google.com/spreadsheets/d/1t4kAuOgT4Oqoldq02rXDrrO2Mwgy80UkcfTBPhnlpK4/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1t4kAuOgT4Oqoldq02rXDrrO2Mwgy80UkcfTBPhnlpK4/edit?usp=sharing)
