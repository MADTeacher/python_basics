from sqlalchemy import ForeignKey, Table, Column

from database.database import Base


association_table = Table(
    "association_table",
    Base.metadata,
    Column("group_id", ForeignKey("group.id", ondelete='CASCADE'),
           primary_key=True),
    Column("discipline_id", ForeignKey("discipline.id", ondelete='CASCADE'),
           primary_key=True),
)
