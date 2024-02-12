# pylint: disable=invalid-name
"""Add Restaurant Dayta

Revision ID: 4096b5e1c05a
Revises: 11b40de5c0cb
Create Date: 2022-12-07 21:44:33.106323

"""
from sqlmodel import Session, create_engine, select

from app.config.database_settings import DatabaseSettings
from app.database.db import assemble_database_url
from app.database.models import Restaurant
from app.utils.csv_utils import csv_import

database_settings = DatabaseSettings()

# revision identifiers, used by Alembic.
revision = "4096b5e1c05a"
down_revision = "11b40de5c0cb"
branch_labels = None
depends_on = None

restaurants: list[Restaurant] = csv_import("alembic/restaurants.csv")


def upgrade() -> None:
    engine = create_engine(assemble_database_url(database_settings, False).unicode_string())

    with Session(engine) as session:
        for restaurant in restaurants:
            session.add(restaurant)
        session.commit()


def downgrade() -> None:
    engine = create_engine(assemble_database_url(database_settings, False).unicode_string())

    with Session(engine) as session:
        for restaurant in restaurants:
            statement = select(Restaurant).where(
                Restaurant.name == restaurant.name,
                Restaurant.open_weekday == restaurant.open_weekday,
                Restaurant.open_time == restaurant.open_time,
                Restaurant.close_weekday == restaurant.close_weekday,
                Restaurant.close_time == restaurant.close_time,
            )
            results = session.exec(statement)
            restaurant = results.one()
            session.delete(restaurant)
        session.commit()
