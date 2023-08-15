#!/usr/bin/env python
from typing import List
from .default import DefaultSettings


class Settings(DefaultSettings):
    INSTALLED_APPS: List[str] = [
        'apps.auth'
    ]


settings = Settings(
    DEBUG=True,
    SECRET_KEY='secret',
    DATABASE_URL='sqlite://server/storages/database/db.sqlite3',
)
