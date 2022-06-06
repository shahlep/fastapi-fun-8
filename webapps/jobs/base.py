from fastapi import APIRouter
from webapps.jobs import routes_jobs

api_router = APIRouter()

api_router.include_router(routes_jobs.router, prefix="", tags=["homepage"])
