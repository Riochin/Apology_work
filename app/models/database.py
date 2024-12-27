import sqlite3
from flask import g

DATABASE = 'C:/Users/Nanako7/Desktop/Apology_work/sample_db.sqlite'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row  # 結果を辞書形式で返す
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def insert_or_delete_db(query, args=()):
    get_db().execute(query, args)
    get_db().commit()

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        # 必要ならテーブルを作成
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year_published INTEGER
            )
        ''')
        conn.commit()
