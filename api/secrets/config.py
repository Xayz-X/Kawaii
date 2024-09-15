from __future__ import annotations


from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str

    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file="api/secrets/.env", extra="ignore"
    )


Config: Settings = Settings()