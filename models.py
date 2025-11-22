from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from database import db

class GuestbookEntry(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(20), nullable=False)
    comment: Mapped[str] = mapped_column(String(255), nullable=False)