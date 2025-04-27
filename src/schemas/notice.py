from pydantic import BaseModel, EmailStr


class NoticeSchema(BaseModel):
    to_mail: EmailStr
    subject: str
    message: str
