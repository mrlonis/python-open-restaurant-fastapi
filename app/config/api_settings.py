from pydantic import BaseSettings


class ApiSettings(BaseSettings):
    # pylint: disable=too-few-public-methods
    log_level: str = "INFO"

    class Config:
        env_file = ".env"
