from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .routes import post_bp

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
    app.register_blueprint(post_bp)  # 投稿用のブループリント

    # アプリケーションのコンテキスト内でインポート
    with app.app_context():
        from .models import Post  # ルートとモデルをインポート
        db.create_all()  # テーブルの作成

    return app
