from flask import Flask
from app.models.database import init_db, insert_or_delete_db  # ここでインポート
from app.routes.routes import bp as main_bp

def create_app():
    app = Flask(__name__)

    # データベース初期化
    init_db()

    # アプリケーションコンテキスト内でデータベース操作
    with app.app_context():
        delete_sql = "DELETE FROM books"
        insert_or_delete_db(delete_sql)

        insert_sql = """
            INSERT INTO books (id, title, author, year_published)
            VALUES 
            (1, 'わたし×IT＝最強説', 'NPO法人Waffle', 2023),
            (2, 'ユウと魔法のプログラミング・ノート', '鳥井雪', 2023),
            (3, 'ハッカーと画家', 'Paul Graham, 川合 史朗', 2005)
        """
        insert_or_delete_db(insert_sql)

    # ルートを登録
    app.register_blueprint(main_bp)

    return app
