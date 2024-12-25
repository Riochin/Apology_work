from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
  pass #これは何にもしないと言う意味

db = SQLAlchemy()

def create_app():
    #　Flaskアプリケーションのインスタンスを作成
    app = Flask(__name__)

    #　アプリケーションの設定
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    #　SQLAlchemyをアプリケーションに初期化
    db.init_app(app)

    # ここでブループリントを登録
    from .routes.blogs_routes import blogs_bp
    # from .routes.comment_routes import comment_bp
    # from .routes.tag_routes import tag_bp

    app.register_blueprint(blogs_bp)
    # app.register_blueprint(comment_bp)
    # app.register_blueprint(tag_bp)

    # アプリケーションのコンテキスト内でインポート
    with app.app_context():
        
        from app.models.blog_models import Blog  # ルートとモデルをインポート
        db.create_all()  # テーブルの作成
        # blogs = Blog.query.all()
        # print(blogs)

        # データベースを検査し、テーブル名を取得して表示
        inspector = inspect(db.engine)
        print(inspector.get_table_names())

    return app
