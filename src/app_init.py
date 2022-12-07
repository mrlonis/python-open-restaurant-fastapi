from typing import Optional

from fastapi import FastAPI

from .config import ApiSettings


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

        return app
