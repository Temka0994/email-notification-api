from fastapi import APIRouter
from src.api.notice import router as notice_router
from src.authentication.users import router as users_router

main_router = APIRouter()

main_router.include_router(notice_router)
main_router.include_router(users_router)
