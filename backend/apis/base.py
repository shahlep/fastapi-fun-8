from fastapi import APIRouter
from backend.apis.version1 import routes_user

api_router = APIRouter()

api_router.include_router(routes_user.router, prefix='/user', tags=['users'])
