from pydantic import BaseModel, Field, field_validator


class NoticeSchema(BaseModel):
    to_mail: str
    subject: str
    message: str
