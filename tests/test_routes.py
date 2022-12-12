from datetime import datetime
from typing import Any, Union, cast

import pytest
from fastapi.testclient import TestClient

from app.database.models import Restaurant


def test_restaurants_route_no_params(test_client_module: TestClient):
    client = test_client_module
    response = client.get("/restaurants")
    assert response.status_code == 200
    restaurants: list[dict] = response.json()
    assert len(restaurants) == 276


def test_restaurants_route_with_datetime_param(test_client_module: TestClient):
    client = test_client_module

    # datetime.now() check for 200 response
    param = datetime.now()
    response = client.get(f"/restaurants?date={param.isoformat()}")
    assert response.status_code == 200

    # Thursday December 8th, 11:11 AM
    param = datetime(2022, 12, 8, 11, 11)
    response = client.get(f"/restaurants?date={param.isoformat()}")
    assert response.status_code == 200
    restaurants: list[dict] = response.json()
    assert len(restaurants) == 23
    restaurant = Restaurant(**restaurants[0])
    assert restaurant.name == "The Cowfish Sushi Burger Bar"

    # Thursday December 8th - No Time
    response = client.get("/restaurants?date=2022-12-08")
    assert response.status_code == 422
    response_json = cast(dict[str, Any], response.json())
    detail_json = cast(Union[list[dict[str, Any]], None], response_json.get("detail"))
    assert detail_json is not None
    assert len(detail_json) == 1
    detail_json_item = detail_json[0]
    assert detail_json_item.get("msg") == "invalid datetime format"

    # Thursday December 8th, 12:00 AM
    param = datetime(2022, 12, 8, 0, 0)
    response = client.get(f"/restaurants?date={param.isoformat()}")
    assert response.status_code == 200
    restaurants: list[dict] = response.json()
    assert len(restaurants) == 0


@pytest.mark.parametrize(
    "hour,minute,total",
    [
        (0, 0, 0),
        (0, 30, 0),
        (1, 0, 0),
        (1, 30, 0),
        (2, 0, 0),
        (2, 30, 0),
        (3, 0, 0),
        (3, 30, 0),
        (4, 0, 0),
        (4, 30, 0),
        (5, 0, 0),
        (5, 30, 0),
        (6, 0, 0),
        (6, 30, 0),
        (7, 0, 0),
        (7, 30, 0),
        (8, 0, 0),
        (8, 30, 0),
        (9, 0, 1),
        (9, 30, 1),
        (10, 0, 2),
        (10, 30, 3),
        (11, 0, 23),
        (11, 30, 35),
        (12, 0, 35),
        (12, 30, 32),
        (13, 0, 32),
        (13, 30, 32),
        (14, 0, 32),
        (14, 30, 32),
        (15, 0, 32),
        (15, 30, 32),
        (16, 0, 32),
        (16, 30, 32),
        (17, 0, 33),
        (17, 30, 33),
        (18, 0, 33),
        (18, 30, 33),
        (19, 0, 33),
        (19, 30, 33),
        (20, 0, 33),
        (20, 30, 33),
        (21, 0, 33),
        (21, 30, 31),
        (22, 0, 26),
        (22, 30, 7),
        (23, 0, 4),
        (23, 30, 0),
    ],
)
def test_restaurants_monday(hour: int, minute: int, total: int, test_client_module: TestClient):
    client = test_client_module

    # Monday December 12th
    param = datetime(2022, 12, 12, hour, minute)
    response = client.get(f"/restaurants?date={param.isoformat()}")
    assert response.status_code == 200
    restaurants: list[dict] = response.json()
    assert len(restaurants) == total


@pytest.mark.parametrize(
    "hour,minute,total",
    [
        (0, 0, 0),
        (0, 30, 0),
        (1, 0, 0),
        (1, 30, 0),
        (2, 0, 0),
        (2, 30, 0),
        (3, 0, 0),
        (3, 30, 0),
        (4, 0, 0),
        (4, 30, 0),
        (5, 0, 0),
        (5, 30, 0),
        (6, 0, 0),
        (6, 30, 0),
        (7, 0, 0),
        (7, 30, 0),
        (8, 0, 0),
        (8, 30, 0),
        (9, 0, 1),
        (9, 30, 1),
        (10, 0, 2),
        (10, 30, 3),
        (11, 0, 22),
        (11, 30, 35),
        (12, 0, 35),
        (12, 30, 32),
        (13, 0, 32),
        (13, 30, 32),
        (14, 0, 32),
        (14, 30, 32),
        (15, 0, 32),
        (15, 30, 32),
        (16, 0, 32),
        (16, 30, 32),
        (17, 0, 33),
        (17, 30, 33),
        (18, 0, 33),
        (18, 30, 33),
        (19, 0, 33),
        (19, 30, 33),
        (20, 0, 33),
        (20, 30, 33),
        (21, 0, 33),
        (21, 30, 31),
        (22, 0, 26),
        (22, 30, 7),
        (23, 0, 4),
        (23, 30, 0),
    ],
)
def test_restaurants_tuesday(hour: int, minute: int, total: int, test_client_module: TestClient):
    client = test_client_module

    # Tuesday December 13th
    param = datetime(2022, 12, 13, hour, minute)
    response = client.get(f"/restaurants?date={param.isoformat()}")
    assert response.status_code == 200
    restaurants: list[dict] = response.json()
    assert len(restaurants) == total


@pytest.mark.parametrize(
    "hour,minute,total",
    [
        (0, 0, 0),
        (0, 30, 0),
        (1, 0, 0),
        (1, 30, 0),
        (2, 0, 0),
        (2, 30, 0),
        (3, 0, 0),
        (3, 30, 0),
        (4, 0, 0),
        (4, 30, 0),
        (5, 0, 0),
        (5, 30, 0),
        (6, 0, 0),
        (6, 30, 0),
        (7, 0, 0),
        (7, 30, 0),
        (8, 0, 0),
        (8, 30, 0),
        (9, 0, 1),
        (9, 30, 1),
        (10, 0, 2),
        (10, 30, 3),
        (11, 0, 23),
        (11, 30, 36),
        (12, 0, 36),
        (12, 30, 33),
        (13, 0, 33),
        (13, 30, 33),
        (14, 0, 33),
        (14, 30, 33),
        (15, 0, 33),
        (15, 30, 33),
        (16, 0, 33),
        (16, 30, 33),
        (17, 0, 34),
        (17, 30, 34),
        (18, 0, 34),
        (18, 30, 34),
        (19, 0, 34),
        (19, 30, 34),
        (20, 0, 34),
        (20, 30, 34),
        (21, 0, 34),
        (21, 30, 32),
        (22, 0, 27),
        (22, 30, 7),
        (23, 0, 4),
        (23, 30, 0),
    ],
)
def test_restaurants_wednesday(hour: int, minute: int, total: int, test_client_module: TestClient):
    client = test_client_module

    # Wednesday December 7th
    param = datetime(2022, 12, 7, hour, minute)
    response = client.get(f"/restaurants?date={param.isoformat()}")
    assert response.status_code == 200
    restaurants: list[dict] = response.json()
    assert len(restaurants) == total


@pytest.mark.parametrize(
    "hour,minute,total",
    [
        (0, 0, 0),
        (0, 30, 0),
        (1, 0, 0),
        (1, 30, 0),
        (2, 0, 0),
        (2, 30, 0),
        (3, 0, 0),
        (3, 30, 0),
        (4, 0, 0),
        (4, 30, 0),
        (5, 0, 0),
        (5, 30, 0),
        (6, 0, 0),
        (6, 30, 0),
        (7, 0, 0),
        (7, 30, 0),
        (8, 0, 0),
        (8, 30, 0),
        (9, 0, 1),
        (9, 30, 1),
        (10, 0, 2),
        (10, 30, 3),
        (11, 0, 23),
        (11, 30, 36),
        (12, 0, 36),
        (12, 30, 33),
        (13, 0, 33),
        (13, 30, 33),
        (14, 0, 33),
        (14, 30, 33),
        (15, 0, 33),
        (15, 30, 33),
        (16, 0, 33),
        (16, 30, 33),
        (17, 0, 34),
        (17, 30, 34),
        (18, 0, 34),
        (18, 30, 34),
        (19, 0, 34),
        (19, 30, 34),
        (20, 0, 34),
        (20, 30, 34),
        (21, 0, 34),
        (21, 30, 32),
        (22, 0, 27),
        (22, 30, 7),
        (23, 0, 4),
        (23, 30, 0),
    ],
)
def test_restaurants_thursday(hour: int, minute: int, total: int, test_client_module: TestClient):
    client = test_client_module

    # Thursday December 8th
    param = datetime(2022, 12, 8, hour, minute)
    response = client.get(f"/restaurants?date={param.isoformat()}")
    assert response.status_code == 200
    restaurants: list[dict] = response.json()
    assert len(restaurants) == total


@pytest.mark.parametrize(
    "hour,minute,total",
    [
        (0, 0, 0),
        (0, 30, 0),
        (1, 0, 0),
        (1, 30, 0),
        (2, 0, 0),
        (2, 30, 0),
        (3, 0, 0),
        (3, 30, 0),
        (4, 0, 0),
        (4, 30, 0),
        (5, 0, 0),
        (5, 30, 0),
        (6, 0, 0),
        (6, 30, 0),
        (7, 0, 0),
        (7, 30, 0),
        (8, 0, 0),
        (8, 30, 0),
        (9, 0, 1),
        (9, 30, 1),
        (10, 0, 3),
        (10, 30, 4),
        (11, 0, 23),
        (11, 30, 36),
        (12, 0, 36),
        (12, 30, 32),
        (13, 0, 31),
        (13, 30, 31),
        (14, 0, 31),
        (14, 30, 31),
        (15, 0, 31),
        (15, 30, 31),
        (16, 0, 31),
        (16, 30, 31),
        (17, 0, 32),
        (17, 30, 32),
        (18, 0, 32),
        (18, 30, 32),
        (19, 0, 32),
        (19, 30, 32),
        (20, 0, 32),
        (20, 30, 32),
        (21, 0, 32),
        (21, 30, 31),
        (22, 0, 27),
        (22, 30, 12),
        (23, 0, 8),
        (23, 30, 0),
    ],
)
def test_restaurants_friday(hour: int, minute: int, total: int, test_client_module: TestClient):
    client = test_client_module

    # Friday December 9th
    param = datetime(2022, 12, 9, hour, minute)
    response = client.get(f"/restaurants?date={param.isoformat()}")
    assert response.status_code == 200
    restaurants: list[dict] = response.json()
    assert len(restaurants) == total


@pytest.mark.parametrize(
    "hour,minute,total",
    [
        (0, 0, 0),
        (0, 30, 0),
        (1, 0, 0),
        (1, 30, 0),
        (2, 0, 0),
        (2, 30, 0),
        (3, 0, 0),
        (3, 30, 0),
        (4, 0, 0),
        (4, 30, 0),
        (5, 0, 0),
        (5, 30, 0),
        (6, 0, 0),
        (6, 30, 0),
        (7, 0, 1),
        (7, 30, 1),
        (8, 0, 1),
        (8, 30, 1),
        (9, 0, 2),
        (9, 30, 3),
        (10, 0, 5),
        (10, 30, 5),
        (11, 0, 22),
        (11, 30, 32),
        (12, 0, 32),
        (12, 30, 28),
        (13, 0, 27),
        (13, 30, 27),
        (14, 0, 27),
        (14, 30, 27),
        (15, 0, 27),
        (15, 30, 26),
        (16, 0, 26),
        (16, 30, 26),
        (17, 0, 29),
        (17, 30, 31),
        (18, 0, 31),
        (18, 30, 31),
        (19, 0, 31),
        (19, 30, 31),
        (20, 0, 31),
        (20, 30, 31),
        (21, 0, 31),
        (21, 30, 30),
        (22, 0, 26),
        (22, 30, 13),
        (23, 0, 9),
        (23, 30, 0),
    ],
)
def test_restaurants_saturday(hour: int, minute: int, total: int, test_client_module: TestClient):
    client = test_client_module

    # Saturday December 10th
    param = datetime(2022, 12, 10, hour, minute)
    response = client.get(f"/restaurants?date={param.isoformat()}")
    assert response.status_code == 200
    restaurants: list[dict] = response.json()
    assert len(restaurants) == total


@pytest.mark.parametrize(
    "hour,minute,total",
    [
        (0, 0, 2),
        (0, 30, 2),
        (1, 0, 2),
        (1, 30, 2),
        (2, 0, 2),
        (2, 30, 1),
        (3, 0, 1),
        (3, 30, 1),
        (4, 0, 1),
        (4, 30, 1),
        (5, 0, 1),
        (5, 30, 1),
        (6, 0, 1),
        (6, 30, 1),
        (7, 0, 2),
        (7, 30, 2),
        (8, 0, 2),
        (8, 30, 2),
        (9, 0, 3),
        (9, 30, 4),
        (10, 0, 6),
        (10, 30, 6),
        (11, 0, 22),
        (11, 30, 32),
        (12, 0, 32),
        (12, 30, 30),
        (13, 0, 30),
        (13, 30, 30),
        (14, 0, 30),
        (14, 30, 30),
        (15, 0, 31),
        (15, 30, 30),
        (16, 0, 30),
        (16, 30, 30),
        (17, 0, 32),
        (17, 30, 33),
        (18, 0, 33),
        (18, 30, 33),
        (19, 0, 33),
        (19, 30, 33),
        (20, 0, 33),
        (20, 30, 33),
        (21, 0, 33),
        (21, 30, 32),
        (22, 0, 27),
        (22, 30, 9),
        (23, 0, 6),
        (23, 30, 1),
    ],
)
def test_restaurants_sunday(hour: int, minute: int, total: int, test_client_module: TestClient):
    client = test_client_module

    # Sunday December 11th
    param = datetime(2022, 12, 11, hour, minute)
    response = client.get(f"/restaurants?date={param.isoformat()}")
    assert response.status_code == 200
    restaurants: list[dict] = response.json()
    assert len(restaurants) == total
