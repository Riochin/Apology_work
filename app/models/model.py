#@title #2.データベースとデータの中身を用意する
import sqlite3

# データベースのテーブル（データを入れるための形のある箱）を用意する
conn = sqlite3.connect('sample_db.sqlite')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year_published INTEGER
)
''')

conn.commit()
conn.close()