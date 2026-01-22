from pydantic_settings import BaseSettings, SettingsConfigDict


class setting(BaseSettings):
    DatabaseURL: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


config= setting()