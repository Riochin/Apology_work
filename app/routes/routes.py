from flask import render_template
from app.database import query_db

def init_routes(app):
    @app.route("/")
    def home():
        #データベースからデータを引き出す（リストのリストの形で帰ってくる）
        books = query_db("SELECT * FROM books")

        # テンプレートにbooks変数を読み出す
        return render_template('home.html', books = books)

    @app.route("/about")
    def about():
        return "<h1>About 1 Page</h1>"
    
    
    #@title #7.アプリケーションでデータを読み出す+テンプレートにデータを渡すプログラミング

