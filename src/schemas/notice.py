from datetime import datetime

from pydantic import BaseModel, EmailStr


class NoticeSchema(BaseModel):
    to_email: EmailStr
    subject: str
    message: str
    scheduled_at: datetime

