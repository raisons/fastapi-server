#!/usr/bin/env python
import math
from functools import cached_property
from typing import TypeVar, Generic, Sequence, Optional

from pydantic import BaseModel
from fastapi import Query
from tortoise.queryset import QuerySet

T = TypeVar("T")


class PaginationParam(BaseModel):
    page: int = Query(default=1, ge=1, description="Page number")
    size: int = Query(default=20, ge=1, le=100, description="Page size")


class PaginationResponse(BaseModel, Generic[T]):
    total: int
    prev: int
    next: int
    page: int
    results: Sequence[T]


class Paginator:

    def __init__(self, object_list: QuerySet, page_size: int):
        self.object_list = object_list
        self.page_size = int(page_size)
        self._total: Optional[int] = None

    @property
    def total(self):
        return self._total

    @cached_property
    def num_pages(self):
        return math.ceil(self.total / self.page_size)

    async def page(self, number: int) -> PaginationResponse:
        if not self._total:
            self._total = await self.object_list.count()

        queryset = self.object_list.offset((number - 1) * self.page_size)
        queryset = queryset.limit(self.page_size)

        return PaginationResponse(
            total=self.total,
            prev=number - 1 if number > 1 else None,
            next=number + 1 if number < self.num_pages else None,
            page=number,
            results=await queryset,
        )
