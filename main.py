import uvicorn
from fastapi import FastAPI
from backend.core.config import settings
from backend.db.session import engine
from backend.db.base import Base
from backend.apis.base import api_router
from webapps.jobs.base import api_router as web_router
from fastapi.staticfiles import StaticFiles


def create_tables():
    Base.metadata.create_all(bind=engine)


def include_router(app):
    app.include_router(api_router)
    app.include_router(web_router)


def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")


def start_application():
    app = FastAPI(
        title=settings.PROJECT_TITLE,
        version=settings.PROJECT_VERSION,
        openapi_url=settings.API_JSON_VERSION,
    )
    create_tables()
    include_router(app)
    configure_static(app)
    return app


app = start_application()

if __name__ == "__main__":
    uvicorn.run(app)
