#!/usr/bin/env python

from tortoise import fields, models, timezone
from starlette.authentication import UnauthenticatedUser
from .base_user import AbstractBaseUser, BaseUserManager


class PermissionsMixin(models.Model):
    is_superuser = fields.BooleanField(default=False)

    class Meta:
        abstract = True


class UserManager(BaseUserManager):

    async def get_user(self, username: str):
        return await self.get_or_none(username=username)

    async def get_active_user(self, username: str):
        return await self.get_or_none(username=username, is_active=True)

    async def create_user(self, username: str, password: str, **kwargs):
        pass

    async def create_superuser(self, username: str, password: str, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        user = await self._model.create(
            username=username,
            **extra_fields
        )
        user.set_password(password)
        await user.save()


class AbstractUser(AbstractBaseUser, PermissionsMixin):
    username = fields.CharField(max_length=20, unique=True)
    nickname = fields.CharField(max_length=50, null=True)
    mobile = fields.CharField(max_length=11, unique=True, null=True)
    email = fields.CharField(max_length=100, unique=True, null=True)
    is_active = fields.BooleanField(default=True)

    date_joined = fields.DatetimeField(default=timezone.now)

    objects = UserManager()

    class Meta:
        abstract = True


class User(AbstractUser):
    id = fields.IntField(pk=True)


class AnonymousUser(UnauthenticatedUser):
    id = None
    pk = None
    username = ""
    is_active = False
    is_superuser = False

    def __str__(self):
        return "AnonymousUser"

    @property
    def is_anonymous(self):
        return True

    @property
    def display_name(self) -> str:
        return self.__str__()


async def get_user(user_id: int):
    user = await User.get_or_none(id=user_id)
    return user or AnonymousUser()
