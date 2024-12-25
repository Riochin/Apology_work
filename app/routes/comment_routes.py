from flask import Blueprint, render_template, redirect, url_for, request, flash
from app import db
from app.models import Blog, Comment

comments_bp = Blueprint('comments', __name__, url_prefix='/blogs/<string:blog_id>/comments')

@comments_bp.route('/')
def comment_index(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    return render_template('comments.html', comments=blog.comments, blog=blog)

@comments_bp.route('/', methods=['POST'])
def comment_create(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    user_name = request.form['user_name']
    body = request.form['body']
    try:
        comment = Comment(blog_id=blog.id, user_name=user_name, body=body)
        db.session.add(comment)
        db.session.commit()
        flash("コメントを追加しました！")
    except Exception as e:
        flash(f"エラーが発生しました: {e}")
    return redirect(url_for('comments.comment_index', blog_id=blog_id))
