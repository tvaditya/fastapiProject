from fastapi import APIRouter

from webapps.jobs import route_jobs

api_router = APIRouter()

api_router.include_router(route_jobs.router, prefix="", tags=["homepage"])

# api_router.include_router(route_users.router, prefix="/user", tags=["users"])
# api_router.include_router(route_jobs.router, prefix="/job", tags=["jobs"])
# api_router.include_router(route_login.router, prefix="/login", tags=["login"])