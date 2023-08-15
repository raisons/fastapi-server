#!/usr/bin/env python
import subprocess
import uvicorn
from typing import Annotated
from typer import Option, Typer
from tortoise import Tortoise, run_async
from server.conf import settings, LOGGING
from server.main import app
from server.db.init_db import init_orm
from server.contrib.auth.models import User

cli = Typer()


@cli.command()
def runserver(host: Annotated[str, Option("--host")] = settings.SERVER_HOST,
              port: Annotated[int, Option("--port", "-p")] = settings.SERVER_PORT):
    uvicorn.run(app, host=host, port=port, log_config=LOGGING)


@cli.command()
def initdb():
    subprocess.run(['aerich', 'init-db'])


@cli.command()
def makemigrations():
    subprocess.run(['aerich', 'migrate'])


@cli.command()
def migrate():
    subprocess.run(['aerich', 'upgrade'])


@cli.command()
def createsuperuser(username: Annotated[str, Option("--username", "-u")] = 'admin',
                    password: Annotated[str, Option("--password", "-p")] = 'admin'):
    init_orm()
    run_async(User.objects.create_superuser(username, password))
