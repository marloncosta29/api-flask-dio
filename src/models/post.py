import sqlalchemy as sa
from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from .base import db
from .user import User

class Post(db.Model):
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    author_id: Mapped[int] = mapped_column(sa.ForeignKey(User.id), nullable=False)
    created: Mapped[datetime] = mapped_column(sa.DateTime, nullable=False, server_default=sa.func.now())
    title: Mapped[str] = mapped_column(sa.String, nullable=False)
    body: Mapped[str] = mapped_column(sa.String, nullable=False)
    
    