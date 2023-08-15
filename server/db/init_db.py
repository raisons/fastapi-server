#!/usr/bin/env python

from tortoise import Tortoise, run_async
from tortoise.contrib.fastapi import register_tortoise
from server.conf import TORTOISE_ORM


def register_orm(app):
    register_tortoise(
        app,
        config=TORTOISE_ORM,
        generate_schemas=True,
        add_exception_handlers=True,
    )


def init_orm():
    run_async(Tortoise.init(config=TORTOISE_ORM))
