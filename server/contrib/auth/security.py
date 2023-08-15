#!/usr/bin/env python
from typing import Union, Optional
from datetime import datetime, timedelta
from fastapi import HTTPException, status, Request, Depends
from fastapi.security import OAuth2PasswordBearer, APIKeyHeader
from jose import JWTError, jwt

from server.conf import settings
from .schemas import TokenPayload, TokenModel
from .models import get_user, User, AnonymousUser

SECRET_KEY = settings.SECRET_KEY
EXPIRE_MINUTES = 60 * 24  # 1 day

token_security = OAuth2PasswordBearer(tokenUrl=f"{settings.API_PREFIX}/auth/token")


def token_decode(token: Optional[str]) -> TokenPayload:
    payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    return TokenPayload.model_validate(payload)


def token_encode(payload: TokenPayload) -> TokenModel:
    payload.exp = datetime.utcnow() + timedelta(minutes=EXPIRE_MINUTES)
    access_token = jwt.encode(
        payload.model_dump(),
        SECRET_KEY,
        algorithm="HS256"
    )
    return TokenModel(access_token=access_token, token_type="bearer")
