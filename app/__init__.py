import os
from flask import Flask, render_template
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

# .envファイルから環境変数を読み込む
load_dotenv()

# Flask アプリの設定
def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    db = SQLAlchemy(app)

    # モジュールのインポート
    from app.database import close_connection
    from app.routes.routes import init_routes

    # teardown_appcontext の登録
    app.teardown_appcontext(close_connection)

    # ルートの初期化
    init_routes(app)
    
    return app

#@title #6.データベースにデータを登録する

