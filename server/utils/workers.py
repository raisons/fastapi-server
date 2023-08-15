#!/usr/bin/env python

from uvicorn.workers import UvicornWorker as _UvicornWorker
from conf import LOGGING


class UvicornWorker(_UvicornWorker):
    CONFIG_KWARGS = {
        "log_config": LOGGING,
    }
