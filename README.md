# Apology_work

ディレクトリ構成例

MyProject/
├── app/
│   ├── __init__.py        # アプリケーションの初期化
│   ├── routes/
│   │   ├── __init__.py    # Blueprint の登録
│   │   ├── post_routes.py # 投稿機能関連のルート
│   │   ├── bookmark_routes.py # ブックマーク機能関連のルート
│   ├── models/
│   │   ├── __init__.py    # モデルの初期化
│   │   ├── post.py        # 投稿機能のデータモデル
│   │   ├── bookmark.py    # ブックマーク機能のデータモデル
│   ├── templates/         # HTML テンプレート
│   ├── static/            # 静的ファイル（CSS, JS など）
└── run.py                 # アプリケーションのエントリポイント

# プロジェクトセットアップガイド

このガイドでは、プロジェクトをローカル環境でセットアップするための手順を説明します。

## 1. 仮想環境（venv）の構築

仮想環境は、プロジェクトごとに依存関係を管理できる環境を作るために使用します。以下のサイトがわかりやすかったです。

https://qiita.com/fiftystorm36/items/b2fd47cf32c7694adc2e

https://qiita.com/shun_sakamoto/items/7944d0ac4d30edf91fde

## 2. Flaskのインストール

仮想環境ができたら、

$ python3 pip install flask

でFlaskをインストールしてあげてください。
続けて、

$ pip install Flask-SQLAlchemy openai==1.55.3 httpx==0.27.2 anyio==3.7.0    

でSQLAlchemyとFlaskをインストールしてください。これでうまくいってほしい、、、