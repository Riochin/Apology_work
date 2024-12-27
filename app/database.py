import sqlite3
from flask import g, render_template
from app import create_app


DATABASE = 'sample_db.sqlite'

def get_db():
    print("データベースに接続します。")
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    print("データベースに接続しました。")
    return db

def close_connection(exception):
    print("データベースの接続を閉じます。")
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    print("データベースからデータを取得します。")
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def insert_or_delete_db(query, args=()):
    print("データベースにデータを挿入します。")
    db = None
    try:
        # クエリの実行
        db = get_db()
        db.execute(query, args)
        db.commit()  # commit()を呼び出して変更を確定
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")  # エラーをコンソールに表示
        db.rollback()  # エラー時にはロールバック
    finally:
        if db is not None:
            db.close()



# 既存のコードに追加
def initialize_books_data():
    print("データベースの初期化を開始します。")
    """
    データベース内の書籍データを初期化する関数。
    """
    app = create_app()
    with app.app_context():
        # この中でデータベース操作を行う
        try:
            delete_sql = "DELETE FROM books"
            insert_or_delete_db(delete_sql)  # booksテーブルを初期化
            insert_sql = """
                INSERT INTO books (id, title, author, year_published)
                VALUES 
                (1, 'わたし×IT＝最強説', 'NPO法人Waffle', 2023),
                (2, 'ユウと魔法のプログラミング・ノート', '鳥井雪', 2023),
                (3, 'ハッカーと画家', 'Paul Graham, 川合 史朗', 2005)
            """
            insert_or_delete_db(insert_sql)  # データを挿入
            print("データが正常に挿入されました。")  # 挿入完了メッセージ
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")  # エラーメッセージを表示


def create_books_table():
    """
    books テーブルを作成する関数。
    """
    create_table_sql = """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year_published INTEGER
        )
    """
    insert_or_delete_db(create_table_sql)
