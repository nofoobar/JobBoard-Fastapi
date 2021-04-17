from apis.version1 import route_jobs
from apis.version1 import route_login
from apis.version1 import route_users
from fastapi import APIRouter


api_router = APIRouter()
api_router.include_router(route_users.router, prefix="/users", tags=["users"])
api_router.include_router(route_jobs.router, prefix="/jobs", tags=["jobs"])
api_router.include_router(route_login.router, prefix="/login", tags=["login"])
