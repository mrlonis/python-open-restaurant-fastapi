from app.csv_utils import csv_import


def test_csv_import():
    restaurants = csv_import()
    assert len(restaurants) == 276
