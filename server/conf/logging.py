#!/usr/bin/env python

from .path import path

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    'filters': {
        'require_debug_true': {
            '()': 'server.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'server.utils.log.RequireDebugFalse',
        }
    },
    'formatters': {
        'access': {
            "()": "uvicorn.logging.AccessFormatter",
            "fmt": '%(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s',
        },
        'console': {
            'format': '%(message)s'
        },
        'file': {
            'format': '%(asctime)s | %(levelname)-7s | %(process)d | %(message)s | %(filename)s:%(lineno)-3d'
        }
    },
    'handlers': {
        'console': {
            'formatter': 'console',
            'level': 'DEBUG',
            'class': 'rich.logging.RichHandler',
            'log_time_format': '[%Y/%m/%d %H:%M:%S]',
            'filters': ['require_debug_true'],
            'omit_repeated_times': False,
            'rich_tracebacks': True,
            'tracebacks_show_locals': True,
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filters': ['require_debug_false'],
            'formatter': 'file',
            'filename': str(path.LOG_DIR / 'fastapi.log'),
            'when': 'midnight',
            'backupCount': 64,
            'encoding': 'utf-8',
        },
        'access': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filters': ['require_debug_false'],
            'formatter': 'file',
            'filename': str(path.LOG_DIR / 'access.log'),
            'when': 'midnight',
            'backupCount': 64,
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        'server': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
        "uvicorn": {
            "handlers": ["console", "access"],
            "level": "INFO",
            "propagate": False,
        },
        "uvicorn.access": {
            "handlers": ["console", "access"],
            "level": "INFO",
            "propagate": False
        },
    },
}
