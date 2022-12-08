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
            statement = statement.where(
                Restaurant.weekday == date.weekday(),
                Restaurant.open <= query_time,
                Restaurant.close >= query_time,
            )

        result = await session.execute(statement)
        restaurants = result.scalars().all()
        return [
            Restaurant(
                id=restaurant.id,
                name=restaurant.name,
                weekday=restaurant.weekday,
                open=restaurant.open,
                close=restaurant.close,
            )
            for restaurant in restaurants
        ]
