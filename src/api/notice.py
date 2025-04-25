import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from fastapi import APIRouter
from src.properties import from_mail, from_mail_password, host, port
from src.schemas.notice import NoticeSchema

router = APIRouter(tags=["Notice"])


@router.post('/notice/', summary="Schedules to send a notice.")
async def send_notice(data: NoticeSchema):

    msg = MIMEMultipart()
    msg['Subject'] = data.subject
    msg['From'] = from_mail
    msg['To'] = data.to_mail
    msg.attach(MIMEText(data.message))

    with smtplib.SMTP(host, port) as server:
        server.starttls()
        server.login(from_mail, from_mail_password)
        server.send_message(msg)


