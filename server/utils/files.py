#!/usr/bin/env python

import aiofiles
from pathlib import Path
from typing import Union
from fastapi import HTTPException, UploadFile

from conf import settings


async def save_file(file: bytes, relative_filepath: Union[str, Path]) -> str:
    if isinstance(relative_filepath, str):
        relative_filepath = Path(relative_filepath)
    filepath = settings.STORAGES_DIR.joinpath(relative_filepath)
    try:
        async with aiofiles.open(filepath, "wb") as f:
            await f.write(file)
    except Exception as e:
        raise HTTPException(status_code=500)
    return str(filepath)
