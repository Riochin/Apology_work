
from flask import Blueprint, redirect, url_for, request, flash
from app import db
from app.models import Blog, Tag

tags_bp = Blueprint('tags', __name__, url_prefix='/blogs/<string:blog_id>/tags')

@tags_bp.route('/', methods=['POST'])
def create_tag(blog_id):
    blogs = Blog.query.get_or_404(blog_id)
    tag_name = request.form['name']
    tag = Tag.query.filter_by(name=tag_name).first()
    if not tag:
        tag = Tag(name=tag_name)
        db.session.add(tag)
    blogs.tags.append(tag)
    db.session.commit()
    flash("タグを追加しました！")
    return redirect(url_for('blogs.blog_index'))
