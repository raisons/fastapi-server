#!/usr/bin/env python
import uuid
from tortoise import manager, models, fields


class Manager(manager.Manager):
    pass


class BaseModel(models.Model):
    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    objects = Manager()

    class Meta:
        abstract = True


class UUIDModel(BaseModel):
    id = fields.UUIDField(pk=True, default=uuid.uuid4)

    class Meta:
        abstract = True
