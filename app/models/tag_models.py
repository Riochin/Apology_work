from app import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.orm import validates
from .association import association_table

class Tag(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    created_at: Mapped[int] = db.Column(db.DateTime(timezone=True))
    blogs: Mapped[list] = relationship(secondary=association_table)

    @validates("name")
    def validate_existance(self, key, value):
        if not value:
            raise ValueError(f"{key} cannot be empty")
        return value
