import datetime

from app.extensions import db
from sqlalchemy import SmallInteger, String, DateTime
from sqlalchemy.orm import mapped_column, Mapped


class Tour(db.Model):
    __tablename__ = 'tours'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    content: Mapped[str]
    image: Mapped[str]
    created_at = mapped_column(DateTime, default=datetime.datetime.now)
    user_id: Mapped[int] = mapped_column(db.ForeignKey('users.id'))
