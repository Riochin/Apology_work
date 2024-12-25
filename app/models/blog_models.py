from app import db
from sqlalchemy.orm import Mapped, mapped_column, validates
from sqlalchemy.orm import relationship
from .association import association_table

class Blog(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    body: Mapped[str] = mapped_column(nullable=False)
    user_name: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[int] = db.Column(db.DateTime(timezone=True))
    # comments = db.relationship('Comment', back_populates='blog')
    # tags: Mapped[list] = relationship(secondary=association_table)

    @validates("title", "body", "user_name")
    def validate_existance(self, key, value):
        if not value:
            raise ValueError(f"{key} cannot be empty")
        return value
