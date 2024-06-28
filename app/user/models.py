from sqlalchemy import SmallInteger, String
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.testing import db
from app.extensions import db


class User(db.Model):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str]

    age: Mapped[int] = mapped_column(SmallInteger)
    address: Mapped[str]
    tours = db.relationship('Tour', backref='user', lazy='dynamic', cascade='all, delete')

    @classmethod
    def get_user_by_email(cls, email):
        user = cls.query.filter_by(email=email).first()
        return user
