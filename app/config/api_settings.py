from pydantic_settings import BaseSettings, SettingsConfigDict


class ApiSettings(BaseSettings):
    # pylint: disable=too-few-public-methods
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    log_level: str = "INFO"
