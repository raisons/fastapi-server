#!/usr/bin/env python
from typing import Annotated
from dataclasses import dataclass
from fastapi import Form
from fastapi.security import OAuth2PasswordRequestForm


@dataclass
class CredentialsForm:
    username: Annotated[str, Form()]
    password: Annotated[str, Form()]
