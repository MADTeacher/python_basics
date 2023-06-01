from datetime import date
from sqlalchemy import ForeignKey, DATE
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.database import Base


class MissedClass(Base):
    __tablename__ = "missed_class"
    id: Mapped[int] = mapped_column(primary_key=True)
    student_id: Mapped[int] = mapped_column(
        ForeignKey("student.id", ondelete='CASCADE')
    )
    discipline_id: Mapped[int] = mapped_column(
        ForeignKey("discipline.id")
    )
    date: Mapped[date] = mapped_column(DATE)
    is_missed: Mapped[bool]

    student: Mapped["Student"] = relationship(
        back_populates="missed"
    )

    def __repr__(self) -> str:
        return f"MissedClass(id={self.id!r}, " \
               f"student_id={self.student_id!r}, " \
               f"discipline_id={self.discipline_id!r}, " \
               f"date={self.date!r})"
    