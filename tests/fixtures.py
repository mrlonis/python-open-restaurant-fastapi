import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.api_settings import ApiSettings
from app.app_init import AppInitializer


@pytest.fixture(scope="function")
def db_session(request) -> str:
    # create and run postgres for the test (requires postgres to be installed
    # and available on the path)
    fix = request.getfixturevalue("postgresql")
    connection = f"postgresql+asyncpg://{fix.info.user}:{fix.info.password}@{fix.info.host}:{fix.info.port}/{fix.info.dbname}"  # pylint: disable=line-too-long
    return connection


@pytest.fixture(name="monkeypatch_session", scope="session")
def monkeypatch_session_():
    """For monkeypatching session level fixtures
    Issue: https://github.com/pytest-dev/pytest/issues/363"""
    # pylint:disable=import-outside-toplevel
    from _pytest.monkeypatch import MonkeyPatch

    mpatch = MonkeyPatch()
    yield mpatch
    mpatch.undo()


def create_app() -> FastAPI:
    the_app: FastAPI = AppInitializer(ApiSettings()).create_app()
    return the_app


@pytest.fixture(name="test_app_module", scope="session")
def test_app_(monkeypatch_session) -> FastAPI:
    """fhir api app test fixture, scoped to the test module"""
    app = create_app()
    return app


def create_test_client(the_app: FastAPI) -> TestClient:
    the_client = TestClient(the_app)
    return the_client


@pytest.fixture(name="test_client_module", scope="session")
def test_client_(test_app_module) -> TestClient:
    """fhir api test client fixture, scoped to the test module"""
    return create_test_client(test_app_module)
