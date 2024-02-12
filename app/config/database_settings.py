from typing import Optional, Union

from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    # pylint: disable=too-few-public-methods
    model_config = SettingsConfigDict(env_file=".env", env_prefix="database_", extra="ignore")

    user: Optional[str] = None
    password: Optional[str] = None
    host: Optional[str] = None
    port: Union[int, str, None] = None
    name: Optional[str] = None
