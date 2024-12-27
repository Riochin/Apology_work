import os
from flask import Flask, g, current_app, render_template
from dotenv import load_dotenv
import sqlite3

# 環境変数の読み込み
load_dotenv()

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(current_app.config['DATABASE'])
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def insert_or_delete_db(query, args=()):
    db = get_db()
    db.execute(query, args)
    db.commit()

def init_db():
    db = get_db()
    
    # テーブルの作成
    cursor = db.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year_published INTEGER
    )
    ''')
    db.commit()

def create_app():
    app = Flask(__name__)
    
    # 設定
    app.config['DATABASE'] = os.path.join(app.instance_path, 'sample_db.sqlite')
    
    # データベース終了処理の登録
    app.teardown_appcontext(close_db)
    
    # Blueprintの登録
    from app.routes import routes
    app.register_blueprint(routes.bp)
    
    # インスタンスフォルダの作成
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
        
    # CLIコマンドの追加
    @app.cli.command('init-db')
    def init_db_command():
        """データベースの初期化とテーブルの作成"""
        init_db()
        print('データベースを初期化しました。')
    
    return app
