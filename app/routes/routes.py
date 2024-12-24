# ページへのアクセスがあった時、どのHTMLを返すかを定義する

from flask import Flask, render_template, request, redirect, url_for

# Flask アプリを作成
app = Flask(__name__)

# ルートの定義
@app.route("/")
def home():
    return "Welcome to the Home Page!"

@app.route("/about")
def about():
    return "This is the About Page!"

#「/index」へアクセスがあった場合に、「index.html」を返す
@app.route("/index")
def index():
    return render_template("index.html")
