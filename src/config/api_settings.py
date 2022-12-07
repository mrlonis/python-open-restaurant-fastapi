from typing import Optional
from pydantic import BaseSettings, Field


class ApiSettings(BaseSettings):
    database_url: Optional[str] = Field(default=None, env="DATABASE_URL")
