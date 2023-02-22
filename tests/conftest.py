import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.app_init import AppInitializer


@pytest.fixture(scope="function")
def db_session(request) -> str:
    # create and run postgres for the test (requires postgres to be installed
    # and available on the path)
    fix = request.getfixturevalue("postgresql")
    print(fix.info)
    connection = (
        f"postgresql+asyncpg://{fix.info.user}:{fix.info.password}@" + f"{fix.info.host}:{fix.info.port}/{fix.info.dbname}"
    )
    return connection


@pytest.fixture(name="test_app_module", scope="session")
def test_app_() -> FastAPI:
    return AppInitializer().create_app()


@pytest.fixture(name="test_client_module", scope="session")
def test_client_(test_app_module) -> TestClient:
    return TestClient(test_app_module)
