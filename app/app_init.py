from typing import Optional

from fastapi import FastAPI

from .routes import load_routes


class AppInitializer:
    # pylint: disable=too-few-public-methods
    def __init__(self):
        self.app: Optional[FastAPI] = None

    def create_app(self):
        """Minimal app setup, used for testing.  Call create_configured_app for production code"""
        self.app = app = FastAPI()
        load_routes(app)
        return app
