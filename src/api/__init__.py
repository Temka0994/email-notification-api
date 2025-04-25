from fastapi import APIRouter
from src.api.notice import router as notice_router

main_router = APIRouter()

main_router.include_router(notice_router)
