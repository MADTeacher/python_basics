from typing import List
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.database import Base


class Student(Base):
    __tablename__ = "student"
    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(50))
    group_id: Mapped[int] = mapped_column(
        ForeignKey("group.id", ondelete='CASCADE')
    )
    group: Mapped["Group"] = relationship(
        back_populates="students"
    )

    missed: Mapped[List["MissedClass"]] = relationship(
        back_populates="student",
        cascade="all, delete, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"Student(id={self.id!r}, name={self.full_name!r}, " \
               f"group_id={self.group_id!r})"