from typing import ClassVar

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "API Python"

    DATABASE_URL: str

    JWT_SECRET: str
    JWT_ALGORITHM: str

    REDIS_HOST: str
    REDIS_PORT: int = 6379

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(
        env_file=".env", extra="ignore"
    )


settings = Settings()  # type: ignore[call-arg]
