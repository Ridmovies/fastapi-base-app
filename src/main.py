from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from src.core.models import db_helper, Base
from src.api import router as api_router
from src.core.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    # async with db_helper.engine.begin() as conn:
    #     # print(f"Creating db_helper")
    #     # await conn.run_sync(Base.metadata.create_all)

    yield
    print(f"Shutting down db_helper")
    await db_helper.dispose()


app = FastAPI(lifespan=lifespan)
app.include_router(api_router, prefix=settings.api.api_prefix)

@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host=settings.run.host, port=settings.run.port)