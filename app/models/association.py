from sqlalchemy import Table, Column, ForeignKey
from app import db

association_table = Table(
    "blog_tag",
    db.metadata,
    Column("blog_id", ForeignKey("blog.id")),
    Column("tag_id", ForeignKey("tag.id"))
)