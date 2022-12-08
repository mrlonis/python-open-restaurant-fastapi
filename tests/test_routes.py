from datetime import datetime
from typing import Any, Union, cast

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

    response = client.get("/restaurants?date=2022-12-8")
    assert response.status_code == 422
    response_json = cast(dict[str, Any], response.json())
    detail_json = cast(Union[list[dict[str, Any]], None], response_json.get("detail"))
    assert detail_json is not None
    assert len(detail_json) == 1
    detail_json_item = detail_json[0]
    assert detail_json_item.get("msg") == "invalid datetime format"
