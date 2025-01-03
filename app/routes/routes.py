from flask import Blueprint, render_template
from app.models.database import query_db  # 修正

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    books = query_db("SELECT * FROM books")
    return render_template('home.html', books=books)

@bp.route('/about')
def about():
    return "<h1>About Page</h1>"
