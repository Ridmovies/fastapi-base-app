from fastapi import APIRouter

from src.core.config import settings
from .users import router as users_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router = APIRouter(
    prefix=settings.api.prefix,
)

