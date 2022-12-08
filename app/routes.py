from fastapi import Depends, FastAPI
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from .database import Restaurant, get_session


def load_routes(app: FastAPI):
    @app.get("/")
    def read_root():
        return {"Hello": "World"}

    @app.get("/restaurants")
    async def get_restaurants(session: AsyncSession = Depends(get_session)):
        result = await session.execute(select(Restaurant))
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
