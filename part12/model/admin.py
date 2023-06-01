from sqlalchemy.orm import Mapped, mapped_column

from database.database import Base


class Admin(Base):
    __tablename__ = "admin"
    telegram_id: Mapped[int] = mapped_column(primary_key=True)

    def __repr__(self) -> str:
        return f"Admin(telegram_id={self.telegram_id!r})"
