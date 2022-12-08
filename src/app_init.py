from typing import Optional

from fastapi import Depends, FastAPI
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from .api_settings import ApiSettings
from .db import get_session
from .models import Restaurant


class AppInitializer:
    # pylint: disable=too-few-public-methods
    def __init__(self, settings: Optional[ApiSettings] = None):
        self.settings = settings or ApiSettings()
        self.app: Optional[FastAPI] = None

    def create_app(self):
        """Minimal app setup, used for testing.  Call create_configured_app for production code"""
        self.app = app = FastAPI()

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

        return app
