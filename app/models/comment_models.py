# @title　#6. Commentモデルを作る
from app import db
from sqlalchemy.orm import validates, Mapped, mapped_column
from sqlalchemy.orm import relationship
from .blog_models import Blog

class Comment(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    blog_id: Mapped[str]  = mapped_column(db.ForeignKey(Blog.id))
    blog = db.relationship('Blog', back_populates='comments') # comment.blogで対象blogを取れる
    body: Mapped[str] = mapped_column(nullable=False)
    user_name: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[int] = db.Column(db.DateTime(timezone=True))

    @validates("blog_id", "body", "user_name")
    def validate_existance(self, key, value):
        if not value:
            raise ValueError(key)

        return value