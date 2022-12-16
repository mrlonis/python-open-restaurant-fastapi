from app.utils.csv_utils import csv_import


def test_csv_import():
    restaurants = csv_import("alembic/restaurants.csv")
    assert len(restaurants) == 276
