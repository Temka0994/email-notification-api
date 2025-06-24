import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from src.properties import from_mail, from_mail_password, host, port
import httpx
from fastapi import APIRouter
from src.schemas.notice import NoticeSchema
from src.models.users import UserModel
from fastapi import Depends
from src.authentication.users import get_current_user
from src.database import SessionDepend
from src.models.notifications import NotificationModel
from sqlalchemy import update, and_, select

router = APIRouter(tags=["Notice"])


@router.post('/notice/', summary="Schedules to send a notice.")
async def post_notice(data: NoticeSchema, postgresql_db: SessionDepend,
                      current_user: UserModel = Depends(get_current_user)):
    new_notice = NotificationModel(
        user_id=current_user.user_id,
        to_email=data.to_email,
        subject=data.subject,
        message=data.message,
        scheduled_at=data.scheduled_at
    )

    postgresql_db.add(new_notice)
    await postgresql_db.commit()

    async with httpx.AsyncClient() as client:
        try:
            await client.post("http://localhost:8001/schedule/", json={
                "body": {
                    "to_email": data.to_email,
                    "subject": data.subject,
                    "message": data.message,
                    "scheduled_at": data.scheduled_at.isoformat()
                },
                "type": "post",
                "callback": 'http://localhost:8000/send_notice/',
                "status": False
            })
        except httpx.ConnectError:
            return {"Error": "Unable to connect to another server."}

    return {"Message": "Scheduled."}


@router.post('/send_notice/', summary="Send a notice at scheduled time.")
async def send_notice(data: NoticeSchema, postgresql_db: SessionDepend):
    check_request = (
        select(NotificationModel)
        .where(
            and_(
                NotificationModel.to_email == data.to_email,
                NotificationModel.subject == data.subject,
                NotificationModel.message == data.message,
                NotificationModel.scheduled_at == data.scheduled_at,
                NotificationModel.status == True
            )
        )
    )

    result = await postgresql_db.execute(check_request)
    notice_status = result.scalars().first()

    if notice_status:
        return {"Message": "Notice already sent."}

    template_path = os.path.join("src", "templates", "notice.html")
    with open(template_path, "r", encoding="utf-8") as file:
        html_template = file.read()

    msg = MIMEMultipart()
    msg['Subject'] = data.subject
    msg['From'] = from_mail
    msg['To'] = data.to_email

    html_content = html_template.replace("{{ message }}", data.message)

    msg.attach(MIMEText(html_content, "html"))

    with smtplib.SMTP(host, port) as server:
        server.starttls()
        server.login(from_mail, from_mail_password)
        server.send_message(msg)

    request = (
        update(NotificationModel)
        .where(
            and_(
                NotificationModel.to_email == data.to_email,
                NotificationModel.subject == data.subject,
                NotificationModel.message == data.message,
                NotificationModel.scheduled_at == data.scheduled_at
            )
        )
        .values(status=True)
    )

    await postgresql_db.execute(request)
    await postgresql_db.commit()

    return {"Message": "Sent."}
