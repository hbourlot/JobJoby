from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from enum import Enum


class Language(Base):
    __tablename__ = "Languages"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
