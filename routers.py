from fastapi import APIRouter
from view.mailer.mailerRouter import mailer_router

main_api_router = APIRouter(prefix='/v1')

main_api_router.include_router(mailer_router, prefix="/email")
