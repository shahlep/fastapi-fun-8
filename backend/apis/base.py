from fastapi import APIRouter
from backend.apis.version1 import routes_user,routes_job

api_router = APIRouter()

api_router.include_router(routes_user.router, prefix="/user", tags=["users"])
api_router.include_router(routes_job.router,prefix="/job",tags=["jobs"])
