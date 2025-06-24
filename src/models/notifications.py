from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text, Boolean, BigInteger, TIMESTAMP, ForeignKey
from datetime import datetime
from src.models.dependencies import Base


class NotificationModel(Base):
    __tablename__ = "notifications"

    notification_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.user_id", ondelete="CASCADE"))
    to_email: Mapped[str] = mapped_column(String(80))
    subject: Mapped[str] = mapped_column(String(80))
    message: Mapped[str] = mapped_column(Text)
    scheduled_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True))
    status: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), default=datetime.utcnow)
