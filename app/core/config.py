from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AI Knowledge Assistant"
    app_version: str = "0.1.0"

    environment: str = "development"

    host: str = "127.0.0.1"
    port: int = 8000

    openai_api_key: str = ""

    model_name: str = "gpt-4o-mini"

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()