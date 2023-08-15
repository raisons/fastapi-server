#!/usr/bin/env python
import logging.config
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from server.conf import settings, LOGGING, path
from server.contrib import auth
from server.core.endpoints import router as default_router
from server.db.init_db import register_orm


def create_app(debug=settings.DEBUG):
    app = FastAPI(
        debug=debug,
        title=settings.PROJECT_NAME,
        openapi_url=settings.OPENAPI_URL
    )
    register_orm(app)
    register_routers(app)
    register_logging(app)
    register_mount(app)
    return app


def register_routers(app: FastAPI):
    app.include_router(default_router)
    app.include_router(auth.auth_router, prefix=settings.API_PREFIX)
    app.include_router(auth.user_router, prefix=settings.API_PREFIX)


def register_logging(app: FastAPI):
    logging.config.dictConfig(LOGGING)


def register_mount(app: FastAPI):
    if settings.DEBUG:
        app.mount('/static', StaticFiles(directory=path.STORAGES_DIR), name='static')


app = create_app()
