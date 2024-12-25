import os
from flask import Flask, render_template
from dotenv import load_dotenv
from pyngrok import ngrok, conf

# .envファイルから環境変数を読み込む
load_dotenv()

# ngrokの認証トークンを設定
conf.get_default().auth_token = os.getenv("NGROK_AUTH_TOKEN")

# Flask アプリの設定
app = Flask(__name__, template_folder="templates", static_folder="static")

# ルートパスへのルーティング
@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    # ngrok を起動して公開URLを取得
    public_url = ngrok.connect(5000)
    print(f"ngrok URL: {public_url}")
    app.run(port=5000)
