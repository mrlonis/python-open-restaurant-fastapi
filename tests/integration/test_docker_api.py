from datetime import datetime
import httpx


def test_docker_api_root_path():
    response = httpx.get("http://0.0.0.0:8008")
    assert response.status_code == 200
    response_json: dict[str, str] = response.json()
    result = response_json.get("Hello")
    assert result == "World"


def test_docker_api_restaurants_route_no_params():
    response = httpx.get("http://0.0.0.0:8008/restaurants")
    assert response.status_code == 200
    restaurants: list[dict] = response.json()
    assert len(restaurants) == 276


def test_restaurants_route_with_datetime_param():

    param = datetime.now()
    response = httpx.get(f"http://0.0.0.0:8008/restaurants?date={param.isoformat()}")
    assert response.status_code == 200

    param = datetime(2022, 12, 8, 11, 11)  # Thursday
    response = httpx.get(f"http://0.0.0.0:8008/restaurants?date={param.isoformat()}")
    assert response.status_code == 200
    restaurants: list[dict] = response.json()
    assert len(restaurants) == 23
