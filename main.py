import uvicorn
from fastapi import FastAPI
from backend.core.config import settings
from backend.db.session import engine
from backend.db.base import Base
from backend.apis.version1.routes_user import router


def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    create_tables()
    app.include_router(router)
    return app


app = start_application()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run(app)
