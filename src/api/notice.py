import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from fastapi import APIRouter
from src.properties import from_mail, from_mail_password, host, port
from src.schemas.notice import NoticeSchema

router = APIRouter(tags=["Notice"])


@router.post('/notice/', summary="Schedules to send a notice.")
async def send_notice(data: NoticeSchema):
    template_path = os.path.join("src", "templates", "notice.html")
    with open(template_path, "r", encoding="utf-8") as file:
        html_template = file.read()

    msg = MIMEMultipart()
    msg['Subject'] = data.subject
    msg['From'] = from_mail
    msg['To'] = data.to_mail

    html_content = html_template.replace("{{ message }}", data.message)

    msg.attach(MIMEText(html_content, "html"))

    with smtplib.SMTP(host, port) as server:
        server.starttls()
        server.login(from_mail, from_mail_password)
        server.send_message(msg)

    return {"message": "ok"}
