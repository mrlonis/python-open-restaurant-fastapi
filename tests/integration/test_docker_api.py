import httpx


def test_docker_api_root_path():
    response = httpx.get("http://0.0.0.0:8008")
    assert response.status_code == 200
    response_json: dict[str, str] = response.json()
    result = response_json.get("Hello")
    assert result == "World"


def test_docker_api_restaurants_route():
    response = httpx.get("http://0.0.0.0:8008/restaurants")
    assert response.status_code == 200
    restaurants: list[dict] = response.json()
    assert len(restaurants) == 276
