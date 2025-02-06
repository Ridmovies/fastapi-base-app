import uvicorn
from fastapi import FastAPI

from src.api import router as api_router
from src.core.config import settings

app = FastAPI()
app.include_router(api_router, prefix=settings.api.api_prefix)

@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8000)