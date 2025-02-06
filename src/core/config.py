from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    users: str = "/users"

class ApiPrefix(BaseModel):
    api_prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()


class DatabaseConfig(BaseModel):
    url: PostgresDsn = "postgresql+asyncpg://user:password@localhost:5435/shop"
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10



class Settings(BaseSettings):
    # DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=(".env.template", ".env"),
        # case_sensitive=False,
        # env_nested_delimiter="__",
        # env_prefix="APP_CONFIG__",
        # env_file=".env",
    )

    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig = DatabaseConfig()


settings = Settings()