#!/usr/bin/env python

from fastapi import APIRouter, Depends
from .dependencies import authenticate, login_required
from .security import token_encode
from .models import User
from .schemas import TokenModel, TokenPayload, ProfileModel
from .forms import CredentialsForm

auth_router = APIRouter(prefix='/auth', tags=['auth'])
user_router = APIRouter(prefix='/user', tags=['user'])


@auth_router.post("/token")
async def create_access_token(form: CredentialsForm = Depends()) -> TokenModel:
    user = await authenticate(username=form.username, password=form.password)

    return token_encode(TokenPayload(
        sub=user.username,
        user_id=user.id,
        username=user.username,
    ))


@user_router.get("/profile")
async def get_profile(user: User = Depends(login_required)) -> ProfileModel:
    return ProfileModel.model_validate(user)
