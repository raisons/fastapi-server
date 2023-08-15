#!/usr/bin/env python

from .optional import settings

TORTOISE_ORM = {
    'connections': {
        'default': settings.DATABASE_URL
    },
    'apps': {
        'auth': {
            'models': [
                'server.contrib.auth.models',
                'aerich.models'
            ],
            'default_connection': 'default',
        },
    },
    'use_tz': settings.USE_TZ,
    'timezone': settings.TIME_ZONE
}
