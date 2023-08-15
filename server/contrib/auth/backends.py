#!/usr/bin/env python
from typing import Optional
from fastapi import Request, HTTPException, status
from starlette.authentication import AuthenticationBackend

from .models import User


class BasicBackend(AuthenticationBackend):

    async def authenticate(self, request: Request, **credentials) -> Optional[User]:
        username = credentials.get("username")
        password = credentials.get("password")
        user = await User.get_or_none(username=username)
        if user and user.check_password(password):
            return user

        return None
