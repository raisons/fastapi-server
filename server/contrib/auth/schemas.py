#!/usr/bin/env python
from typing import Literal, Optional, TypeVar, Generic
from pydantic import BaseModel, ConfigDict


class ProfileModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    username: Optional[str] = None
    nickname: Optional[str] = None
    avatar: Optional[str] = None


class ProfileUpdateModel(BaseModel):
    nickname: str


class LoginModel(BaseModel):
    username: str
    password: str


class CredentialsModel(BaseModel):
    """
    登录
    """
    username: str
    password: str


class TokenModel(BaseModel):
    """
    登录返回
    """
    access_token: str
    token_type: Literal['bearer'] = 'bearer'


class TokenPayload(BaseModel):
    """
    Token 加密信息
    """
    model_config = ConfigDict(from_attributes=True)

    sub: str
    exp: int = None
    scopes: list = []
    username: str = None
    user_id: int = None
