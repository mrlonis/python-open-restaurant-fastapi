import csv
from datetime import time
from pathlib import Path
from typing import Literal, Optional, cast

from ..database import Restaurant

acronym_map = {
    "Mon": 0,
    "Tues": 1,
    "Wed": 2,
    "Thu": 3,
    "Fri": 4,
    "Sat": 5,
    "Sun": 6,
}


def map_weekday_acronym_to_int(acronym: Literal["Mon", "Tues", "Wed", "Thu", "Fri", "Sat", "Sun"]):
    result = acronym_map.get(acronym)
    assert result is not None
    return result


def csv_import():
    restaurants: list[Restaurant] = []

    with open(Path("alembic/restaurants.csv").resolve(), newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = cast(str, row["Restaurant Name"])
            hours = cast(str, row["Hours"])

            split_hours = hours.split("  / ")
            for split_hour in split_hours:
                comma_split = split_hour.split(", ")
                if len(comma_split) == 1:
                    # No Comma
                    restaurants.extend(_process_csv(comma_split[0], name))
                else:
                    # With Commas
                    assert len(comma_split) == 2
                    additional_weekday_ranges = _process_weekday_range(comma_split[0])
                    restaurants.extend(_process_csv(comma_split[1], name, additional_weekday_ranges))

    return restaurants


def _process_weekday_range(weekday_range: str):
    weekdays: list[int] = []

    if "-" in weekday_range:
        weekday_range_split = weekday_range.split("-")
        assert len(weekday_range_split) == 2
        start_weekday = cast(Literal["Mon", "Tues", "Wed", "Thu", "Fri", "Sat", "Sun"], weekday_range_split[0])
        end_weekday = cast(Literal["Mon", "Tues", "Wed", "Thu", "Fri", "Sat", "Sun"], weekday_range_split[1])
        weekdays = list(range(map_weekday_acronym_to_int(start_weekday), map_weekday_acronym_to_int(end_weekday) + 1))
    else:
        weekday = cast(Literal["Mon", "Tues", "Wed", "Thu", "Fri", "Sat", "Sun"], weekday_range)
        weekdays = [map_weekday_acronym_to_int(weekday)]

    return weekdays


def _process_time(time_str: str, am_pm: str):
    # Check for Colon
    colon_split = time_str.split(":")
    if len(colon_split) == 2:
        return_time = time(int(colon_split[0]), int(colon_split[1]))
    elif len(colon_split) == 1:
        return_time = time(int(colon_split[0]))
    else:
        raise ValueError("Invalid Time")

    # If PM we need to add 12 hours
    if am_pm == "pm":
        hour = return_time.hour + 12
        if hour >= 24:
            # If greater than or equal to 24, set to correct time
            hour = 0

        return_time = time(hour, return_time.minute)

    return return_time


def _process_csv(csv_data: str, name: str, additional_weekday_ranges: Optional[list[int]] = None):
    restaurants: list[Restaurant] = []

    space_split = csv_data.split(" ")
    assert len(space_split) == 6

    # Weekdays
    weekdays = _process_weekday_range(space_split[0])
    if additional_weekday_ranges:
        weekdays.extend(additional_weekday_ranges)

    # Open Time
    open_time = _process_time(space_split[1], space_split[2])

    # Close Time
    close_time = _process_time(space_split[4], space_split[5])

    # Build Restaurant
    for weekday in weekdays:
        temp_restaurant = Restaurant(
            name=name,
            weekday=weekday,
            open=open_time,
            close=close_time,
        )
        restaurants.append(temp_restaurant)

    return restaurants
