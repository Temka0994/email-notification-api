from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text
from src.models.dependencies import Base


class UserModel(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(80), unique=True)
    password: Mapped[str] = mapped_column(Text)
