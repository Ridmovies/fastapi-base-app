from fastapi import APIRouter

from src.core.config import settings

router = APIRouter(
    prefix=settings.api.v1.users,
    tags=["users"],
)


@router.get("/")
async def root():
    return {"message": "Hello World"}
