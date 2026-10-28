from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text


class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    company: Mapped[str]
    url: Mapped[str]
    raw_text: Mapped[str | None] = mapped_column(Text)
    source: Mapped[str]
