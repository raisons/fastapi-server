#!/usr/bin/env python
import inspect
from typing import Annotated
from fastapi import Depends, HTTPException, status, Request

from server.conf import settings
from .models import User, get_user
from .security import token_security, token_decode
from .backends import BasicBackend


async def authenticate(request: Request = None, **credentials) -> User:
    backend = BasicBackend()
    user = await backend.authenticate(request, **credentials)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def login_required(token: str = Depends(token_security)) -> User:
    payload = token_decode(token)
    user = await get_user(payload.user_id)
    if not user.is_authenticated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user",
        )

    return user


async def superuser_required(user: User = Depends(login_required)) -> User:
    if not user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Superuser required",
        )
    return user
