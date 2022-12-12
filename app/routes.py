from datetime import datetime
from typing import Optional

from fastapi import Depends, FastAPI
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from .database import Restaurant, get_session


def load_routes(app: FastAPI):
    @app.get("/")
    async def read_root():
        return {"Hello": "World"}

    @app.get("/restaurants")
    async def get_open_restaurants(date: Optional[datetime] = None, session: AsyncSession = Depends(get_session)):
        statement = select(Restaurant)

        if date:
            query_time = date.time()
            weekday = date.weekday()

            statement = statement.where(
                (
                    ((Restaurant.open_weekday == weekday) & (Restaurant.open_time <= query_time))
                    | (Restaurant.open_weekday < weekday)
                )
                & (
                    ((Restaurant.close_weekday == weekday) & (Restaurant.close_time >= query_time))
                    | (Restaurant.close_weekday > weekday)
                ),
            )

        result = await session.execute(statement)
        restaurants = result.scalars().all()
        return [
            Restaurant(
                id=restaurant.id,
                name=restaurant.name,
                open_weekday=restaurant.open_weekday,
                open_time=restaurant.open_time,
                close_weekday=restaurant.close_weekday,
                close_time=restaurant.close_time,
            )
            for restaurant in restaurants
        ]
