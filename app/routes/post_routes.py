# routes/post_routes.py
from flask import Blueprint, render_template

post_bp = Blueprint('post', __name__)

@post_bp.route('/post')
def post():
    return render_template('post.html')
