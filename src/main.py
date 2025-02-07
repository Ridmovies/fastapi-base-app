from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from src.core.models import db_helper, Base
from src.api import router as api_router
from src.core.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    print(f"Shutting down db_helper")
    await db_helper.dispose()


app = FastAPI(
    lifespan=lifespan,
    default_response_class=ORJSONResponse,
)
app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host=settings.run.host, port=settings.run.port)