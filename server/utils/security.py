#!/usr/bin/env python
import random
import string
import secrets

RANDOM_STRING_CHARS = string.ascii_letters + string.digits


def random_string(length, allowed_chars=RANDOM_STRING_CHARS):
    return "".join(secrets.choice(allowed_chars) for i in range(length))


def random_hash(length=12):
    return random_string(length)
