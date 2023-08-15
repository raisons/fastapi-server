#!/usr/bin/env python
import logging
from fastapi import APIRouter

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/")
async def index() -> str:
    logger.info("Hello World!")
    return "Hello World!"
