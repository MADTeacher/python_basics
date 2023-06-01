from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.database import Base
from model.assigned_discipline import association_table


class Group(Base):
    __tablename__ = "group"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(15))
    students: Mapped[List["Student"]] = relationship(
        back_populates="group",
        cascade="all, delete, delete-orphan",
    )

    disciplines: Mapped[List["Discipline"]] = relationship(
        secondary=association_table,
        back_populates="groups",
    )

    def __repr__(self) -> str:
        return f"Group(id={self.id!r}, name={self.name!r})"
