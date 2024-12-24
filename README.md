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

プロジェクトで使用するパッケージはすべて requirements.txt に記載されています。これを使って、他のメンバーが同じパッケージをインストールできます！

仮想環境をアクティブにできたら、以下のコマンドを実行して依存関係をインストールします。

$ pip install -r requirements.txt

これで、プロジェクトに必要なパッケージが全部インストールされる！おそらく

## 3. .envの作成

新しく『.env』ファイルを作成して、.envexampleの内容をコピぺしてください。

中に必要なAPIkeyを入力し、.envexampleには何もAPI keyが書かれていないことを確認してください。絶対にAPIkeyをGit Hub上にPushしないように心がけましょう！

