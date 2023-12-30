from fastapi import APIRouter

mailer_router = APIRouter()


@mailer_router.post("/send-email")
async def schedule_mail(req: MailBody, tasks:):
