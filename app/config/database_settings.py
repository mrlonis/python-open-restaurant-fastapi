from typing import Optional, Union

from pydantic import BaseSettings


class DatabaseSettings(BaseSettings):
    # pylint: disable=too-few-public-methods
    user: Optional[str] = None
    password: Optional[str] = None
    host: Optional[str] = None
    port: Union[int, str, None] = None
    name: Optional[str] = None

    class Config:
        env_file = ".env"
        env_prefix = "database_"
