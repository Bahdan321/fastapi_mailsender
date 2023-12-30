from schemas import MailBody
from other.mailer import send_mail

from fastapi import APIRouter, BackgroundTasks

mailer_router = APIRouter()


@mailer_router.post("/send-email")
async def schedule_mail(req: MailBody, tasks: BackgroundTasks):
    data = req.model_dump()
    tasks.add_task(send_mail, data)
    return {
        "status": 200,
        "message": "email has been scheduled",
    }
