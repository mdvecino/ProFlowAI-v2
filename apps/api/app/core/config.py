from functools import lru_cache

from pydantic import AliasChoices, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = Field(default="ProFlowAI API", validation_alias=AliasChoices("PROJECT_NAME", "APP_NAME"))
    api_v1_prefix: str = Field(default="/api/v1", validation_alias=AliasChoices("API_V1_PREFIX"))
    environment: str = "development"
    debug: bool = True

    secret_key: str = Field(..., min_length=32, validation_alias=AliasChoices("JWT_SECRET_KEY", "SECRET_KEY"))
    access_token_expire_minutes: int = 60
    algorithm: str = Field(default="HS256", validation_alias=AliasChoices("JWT_ALGORITHM", "ALGORITHM"))

    postgres_server: str = "db"
    postgres_port: int = 5432
    postgres_user: str = "proflowai"
    postgres_password: str = "proflowai"
    postgres_db: str = "proflowai"
    database_url: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    @property
    def sqlalchemy_database_uri(self) -> str:
        if self.database_url:
            return self.database_url
        return (
            f"postgresql+psycopg://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_server}:{self.postgres_port}/{self.postgres_db}"
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()
