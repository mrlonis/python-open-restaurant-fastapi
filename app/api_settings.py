from typing import Optional, Union

from pydantic import BaseSettings, Field


class ApiSettings(BaseSettings):
    # pylint: disable=too-few-public-methods
    database_user: Optional[str] = Field(default=None, env="DATABASE_USER")
    database_password: Optional[str] = Field(default=None, env="DATABASE_PASSWORD")
    database_host: Optional[str] = Field(default=None, env="DATABASE_HOST")
    database_port: Union[int, str, None] = Field(default=None, env="DATABASE_PORT")
    database_name: Optional[str] = Field(default=None, env="DATABASE_NAME")

    class Config:
        case_sensitive = True
        env_file = ".env"
