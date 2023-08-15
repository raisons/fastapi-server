#!/usr/bin/env python
from typing import Union, List
from pydantic import PostgresDsn, MySQLDsn, IPvAnyAddress, ImportString
from pydantic_settings import BaseSettings, SettingsConfigDict

DatabaseDsn = Union[PostgresDsn, MySQLDsn, str]


class DefaultSettings(BaseSettings):
    """
    Settings for the FastAPI server.

    environment variables will always take priority over values loaded from a dotenv file!
    """
    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="",
        env_nested_delimiter="__",
        case_sensitive=True,
    )

    DEBUG: bool = False

    PROJECT_NAME: str = "FastAPI Server"

    VERSION: str = "0.0.1"

    API_VERSION: str = "v1"

    API_PREFIX: str = f"/api/{API_VERSION}"

    OPENAPI_URL: str = f"{API_PREFIX}/openapi.json"

    SECRET_KEY: str

    SERVER_NAME: str = PROJECT_NAME

    SERVER_HOST: IPvAnyAddress = "127.0.0.1"

    SERVER_PORT: int = 5555

    # Local time zone
    TIME_ZONE: str = "Asia/Shanghai"
    USE_TZ: bool = False

    INSTALLED_APPS: List[str] = []

    # Database
    DATABASE_URL: DatabaseDsn

    AUTH_TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 24 * 7  # 7 days

    AUTH_TOKEN_SECRET_KEY: str = "secret"

    AUTH_TOKEN_ALGORITHM: str = "HS256"
