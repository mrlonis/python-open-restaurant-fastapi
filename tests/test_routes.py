from datetime import datetime

from fastapi.testclient import TestClient


def test_restaurants_route_no_params(test_client_module: TestClient):
    client = test_client_module
    response = client.get("/restaurants")
    assert response.status_code == 200
    restaurants: list[dict] = response.json()
    assert len(restaurants) == 276


def test_restaurants_route_with_datetime_param(test_client_module: TestClient):
    client = test_client_module

    param = datetime.now()
    response = client.get(f"/restaurants?date={param.isoformat()}")
    assert response.status_code == 200

    param = datetime(2022, 12, 8, 11, 11)  # Thursday
    response = client.get(f"/restaurants?date={param.isoformat()}")
    assert response.status_code == 200
    restaurants: list[dict] = response.json()
    assert len(restaurants) == 23
