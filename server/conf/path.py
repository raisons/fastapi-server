#!/usr/bin/env python
import pathlib
from pydantic import BaseModel, field_validator


class Path(BaseModel):
    BASE_DIR: pathlib.Path = pathlib.Path(__file__).parent.parent
    STORAGES_DIR: pathlib.Path = BASE_DIR / "storages"
    DB_DIR: pathlib.Path = STORAGES_DIR / "database"
    LOG_DIR: pathlib.Path = STORAGES_DIR / "logs"
    UPLOAD_DIR: pathlib.Path = STORAGES_DIR / "uploads"

    @field_validator('BASE_DIR')
    def check_base_dir(cls, v: pathlib.Path):
        if v.name != 'server':
            raise ValueError('BASE_DIR must be the parent directory of server')
        return v


path = Path()
