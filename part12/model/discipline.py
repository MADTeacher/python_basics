from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from database.database import Base
from model.assigned_discipline import association_table


class Discipline(Base):
    __tablename__ = "discipline"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(150))

    groups: Mapped[List["Group"]] = relationship(
        secondary=association_table, back_populates="disciplines"
    )

    def __repr__(self) -> str:
        return f"Discipline(id={self.id!r}, name={self.name!r})"
