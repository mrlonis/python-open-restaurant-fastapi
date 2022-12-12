from datetime import datetime
from typing import Any, Union, cast

import httpx
import pytest

from app.database.models import Restaurant


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
    # datetime.now() check for 200 response
    param = datetime.now()
    response = httpx.get(f"http://0.0.0.0:8008/restaurants?date={param.isoformat()}")
    assert response.status_code == 200

    # Thursday December 8th, 11:11 AM
    param = datetime(2022, 12, 8, 11, 11)  # Thursday
    response = httpx.get(f"http://0.0.0.0:8008/restaurants?date={param.isoformat()}")
    assert response.status_code == 200
    restaurants: list[dict] = response.json()
    assert len(restaurants) == 25
    restaurant = Restaurant(**restaurants[0])
    assert restaurant.name == "The Cowfish Sushi Burger Bar"

    # Thursday December 8th - No Time
    response = httpx.get("http://0.0.0.0:8008/restaurants?date=2022-12-8")
    assert response.status_code == 422
    response_json = cast(dict[str, Any], response.json())
    detail_json = cast(Union[list[dict[str, Any]], None], response_json.get("detail"))
    assert detail_json is not None
    assert len(detail_json) == 1
    detail_json_item = detail_json[0]
    assert detail_json_item.get("msg") == "invalid datetime format"

    # Thursday December 8th, 12:00 AM
    param = datetime(2022, 12, 8, 0, 0)
    response = httpx.get(f"http://0.0.0.0:8008/restaurants?date={param.isoformat()}")
    assert response.status_code == 200
    restaurants: list[dict] = response.json()
    assert len(restaurants) == 5


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
        (11, 0, 25),
        (11, 30, 37),
        (12, 0, 37),
        (12, 30, 36),
        (13, 0, 36),
        (13, 30, 36),
        (14, 0, 36),
        (14, 30, 36),
        (15, 0, 36),
        (15, 30, 36),
        (16, 0, 36),
        (16, 30, 36),
        (17, 0, 38),
        (17, 30, 38),
        (18, 0, 38),
        (18, 30, 38),
        (19, 0, 38),
        (19, 30, 38),
        (20, 0, 38),
        (20, 30, 38),
        (21, 0, 38),
        (21, 30, 36),
        (22, 0, 31),
        (22, 30, 12),
        (23, 0, 9),
        (23, 30, 5),
    ],
)
def test_restaurants_monday(hour: int, minute: int, total: int):
    # Monday December 12th
    param = datetime(2022, 12, 12, hour, minute)
    response = httpx.get(f"http://0.0.0.0:8008/restaurants?date={param.isoformat()}")
    assert response.status_code == 200
    restaurants: list[dict] = response.json()
    assert len(restaurants) == total


@pytest.mark.parametrize(
    "hour,minute,total",
    [
        (0, 0, 5),
        (0, 30, 2),
        (1, 0, 1),
        (1, 30, 1),
        (2, 0, 1),
        (2, 30, 1),
        (3, 0, 1),
        (3, 30, 1),
        (4, 0, 1),
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
        (11, 0, 24),
        (11, 30, 37),
        (12, 0, 37),
        (12, 30, 36),
        (13, 0, 36),
        (13, 30, 36),
        (14, 0, 36),
        (14, 30, 36),
        (15, 0, 36),
        (15, 30, 36),
        (16, 0, 36),
        (16, 30, 36),
        (17, 0, 38),
        (17, 30, 38),
        (18, 0, 38),
        (18, 30, 38),
        (19, 0, 38),
        (19, 30, 38),
        (20, 0, 38),
        (20, 30, 38),
        (21, 0, 38),
        (21, 30, 36),
        (22, 0, 31),
        (22, 30, 12),
        (23, 0, 9),
        (23, 30, 5),
    ],
)
def test_restaurants_tuesday(hour: int, minute: int, total: int):
    # Tuesday December 13th
    param = datetime(2022, 12, 13, hour, minute)
    response = httpx.get(f"http://0.0.0.0:8008/restaurants?date={param.isoformat()}")
    assert response.status_code == 200
    restaurants: list[dict] = response.json()
    assert len(restaurants) == total


@pytest.mark.parametrize(
    "hour,minute,total",
    [
        (0, 0, 5),
        (0, 30, 2),
        (1, 0, 1),
        (1, 30, 1),
        (2, 0, 1),
        (2, 30, 1),
        (3, 0, 1),
        (3, 30, 1),
        (4, 0, 1),
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
        (11, 0, 25),
        (11, 30, 38),
        (12, 0, 38),
        (12, 30, 37),
        (13, 0, 37),
        (13, 30, 37),
        (14, 0, 37),
        (14, 30, 37),
        (15, 0, 37),
        (15, 30, 37),
        (16, 0, 37),
        (16, 30, 37),
        (17, 0, 39),
        (17, 30, 39),
        (18, 0, 39),
        (18, 30, 39),
        (19, 0, 39),
        (19, 30, 39),
        (20, 0, 39),
        (20, 30, 39),
        (21, 0, 39),
        (21, 30, 37),
        (22, 0, 32),
        (22, 30, 12),
        (23, 0, 9),
        (23, 30, 5),
    ],
)
def test_restaurants_wednesday(hour: int, minute: int, total: int):
    # Wednesday December 7th
    param = datetime(2022, 12, 7, hour, minute)
    response = httpx.get(f"http://0.0.0.0:8008/restaurants?date={param.isoformat()}")
    assert response.status_code == 200
    restaurants: list[dict] = response.json()
    assert len(restaurants) == total


@pytest.mark.parametrize(
    "hour,minute,total",
    [
        (0, 0, 5),
        (0, 30, 2),
        (1, 0, 1),
        (1, 30, 1),
        (2, 0, 1),
        (2, 30, 1),
        (3, 0, 1),
        (3, 30, 1),
        (4, 0, 1),
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
        (11, 0, 25),
        (11, 30, 38),
        (12, 0, 38),
        (12, 30, 37),
        (13, 0, 37),
        (13, 30, 37),
        (14, 0, 37),
        (14, 30, 37),
        (15, 0, 37),
        (15, 30, 37),
        (16, 0, 37),
        (16, 30, 37),
        (17, 0, 39),
        (17, 30, 39),
        (18, 0, 39),
        (18, 30, 39),
        (19, 0, 39),
        (19, 30, 39),
        (20, 0, 39),
        (20, 30, 39),
        (21, 0, 39),
        (21, 30, 37),
        (22, 0, 32),
        (22, 30, 12),
        (23, 0, 9),
        (23, 30, 5),
    ],
)
def test_restaurants_thursday(hour: int, minute: int, total: int):
    # Thursday December 8th
    param = datetime(2022, 12, 8, hour, minute)
    response = httpx.get(f"http://0.0.0.0:8008/restaurants?date={param.isoformat()}")
    assert response.status_code == 200
    restaurants: list[dict] = response.json()
    assert len(restaurants) == total


@pytest.mark.parametrize(
    "hour,minute,total",
    [
        (0, 0, 5),
        (0, 30, 2),
        (1, 0, 2),
        (1, 30, 2),
        (2, 0, 1),
        (2, 30, 1),
        (3, 0, 1),
        (3, 30, 1),
        (4, 0, 1),
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
        (11, 0, 25),
        (11, 30, 38),
        (12, 0, 38),
        (12, 30, 37),
        (13, 0, 37),
        (13, 30, 37),
        (14, 0, 37),
        (14, 30, 37),
        (15, 0, 37),
        (15, 30, 37),
        (16, 0, 37),
        (16, 30, 37),
        (17, 0, 39),
        (17, 30, 39),
        (18, 0, 39),
        (18, 30, 39),
        (19, 0, 39),
        (19, 30, 39),
        (20, 0, 39),
        (20, 30, 39),
        (21, 0, 39),
        (21, 30, 38),
        (22, 0, 34),
        (22, 30, 19),
        (23, 0, 15),
        (23, 30, 7),
    ],
)
def test_restaurants_friday(hour: int, minute: int, total: int):
    # Friday December 9th
    param = datetime(2022, 12, 9, hour, minute)
    response = httpx.get(f"http://0.0.0.0:8008/restaurants?date={param.isoformat()}")
    assert response.status_code == 200
    restaurants: list[dict] = response.json()
    assert len(restaurants) == total


@pytest.mark.parametrize(
    "hour,minute,total",
    [
        (0, 0, 7),
        (0, 30, 3),
        (1, 0, 2),
        (1, 30, 2),
        (2, 0, 1),
        (2, 30, 1),
        (3, 0, 1),
        (3, 30, 1),
        (4, 0, 1),
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
        (11, 0, 24),
        (11, 30, 34),
        (12, 0, 34),
        (12, 30, 33),
        (13, 0, 33),
        (13, 30, 33),
        (14, 0, 33),
        (14, 30, 33),
        (15, 0, 34),
        (15, 30, 33),
        (16, 0, 33),
        (16, 30, 33),
        (17, 0, 36),
        (17, 30, 38),
        (18, 0, 38),
        (18, 30, 38),
        (19, 0, 38),
        (19, 30, 38),
        (20, 0, 38),
        (20, 30, 38),
        (21, 0, 38),
        (21, 30, 37),
        (22, 0, 33),
        (22, 30, 20),
        (23, 0, 16),
        (23, 30, 7),
    ],
)
def test_restaurants_saturday(hour: int, minute: int, total: int):
    # Saturday December 10th
    param = datetime(2022, 12, 10, hour, minute)
    response = httpx.get(f"http://0.0.0.0:8008/restaurants?date={param.isoformat()}")
    assert response.status_code == 200
    restaurants: list[dict] = response.json()
    assert len(restaurants) == total


@pytest.mark.parametrize(
    "hour,minute,total",
    [
        (0, 0, 7),
        (0, 30, 3),
        (1, 0, 2),
        (1, 30, 2),
        (2, 0, 1),
        (2, 30, 1),
        (3, 0, 1),
        (3, 30, 1),
        (4, 0, 1),
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
        (11, 0, 19),
        (11, 30, 29),
        (12, 0, 30),
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
def test_restaurants_sunday(hour: int, minute: int, total: int):
    # Sunday December 11th
    param = datetime(2022, 12, 11, hour, minute)
    response = httpx.get(f"http://0.0.0.0:8008/restaurants?date={param.isoformat()}")
    assert response.status_code == 200
    restaurants: list[dict] = response.json()
    assert len(restaurants) == total
