import uvicorn
from fastapi import FastAPI
from core.config import settings

app = FastAPI(
    title=settings.PROJECT_TITLE,
    version=settings.PROJECT_VERSION)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run(app)
