from flask import Blueprint, render_template, redirect, url_for, request, flash
from app import db
from app.models import Blog
# from app.models import Tag

blogs_bp = Blueprint('blogs', __name__, url_prefix='/blogs')

# @blogs_bp.route('/', methods=['GET'])
# def home():
#     return "Blog Home"

@blogs_bp.route('/', methods=['GET'])
def blog_index():
    blogs = Blog.query.all()
    # tags = Tag.query.all()

    #テンプレートにblogs変数を渡す
    return render_template('index.html', blogs=blogs, blog = Blog)

@blogs_bp.route('/blogs', methods=['POST'])
def blog_create():

    # フォームの値を取得してバリデーションを行う
    title = request.form['title']
    user_name = request.form['user_name']
    body = request.form['body']
    try:
        blog = Blog(title=title, user_name=user_name, body=body)
        db.session.add(blog)
        db.session.commit()
        flash("ブログを作成しました！")
    except Exception as e:
        flash(f"エラーが発生しました: {e}")
    # blogs.htmlテンプレートを描画

    blogs = Blog.query.all()
    return render_template('index.html', blogs = blogs, blog = blog)
