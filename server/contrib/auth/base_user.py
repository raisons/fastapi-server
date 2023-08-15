#!/usr/bin/env python

from tortoise import fields, models
from starlette.authentication import BaseUser
from passlib.hash import django_pbkdf2_sha256 as password_hasher
from server.utils.security import random_string


class BaseUserManager(models.Manager):
    @classmethod
    def normalize_email(cls, email):
        """
        Normalize the email address by lower casing the domain part of it.
        """
        email = email or ""
        try:
            email_name, domain_part = email.strip().rsplit("@", 1)
        except ValueError:
            pass
        else:
            email = email_name + "@" + domain_part.lower()
        return email

    @staticmethod
    def make_random_password(
        length=10,
        allowed_chars="abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789",
    ):
        """
        Generate a random password with the given length and given
        allowed_chars. The default value of allowed_chars does not have "I" or
        "O" or letters and digits that look similar -- just to avoid confusion.
        """
        return random_string(length, allowed_chars)


class AbstractBaseUser(BaseUser, models.Model):
    hashed_password = fields.CharField(max_length=128, null=True)
    last_login = fields.DatetimeField(null=True)
    is_active = True

    class Meta:
        abstract = True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    @property
    def display_name(self):
        return self.username

    def set_password(self, password: str):
        self.hashed_password = password_hasher.hash(password)

    def check_password(self, password: str) -> bool:
        return password_hasher.verify(password, self.hashed_password)
