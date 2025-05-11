# ごめんなさい.com 

### 🏆Waffle College卒業ハッカソン最優秀賞受賞

> "まったく新しい謝罪体験"を提供する、
> 謝罪文の『添削』『投稿』『保存』に特化したサービス🙏🌼
>
> 発表スライドは[【こちら】](https://www.canva.com/design/DAGb9swtU5c/6zWu1eixijZKwsgWFDBvkw/edit?utm_content=DAGb9swtU5c&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)‼️
>
> ソースコードは[【こちら】](https://deepnote.com/workspace/Riochins-Workspace-a976ff30-0151-424d-9de2-e20631a0b879/project/ApologyWork-6017cecd-c0c5-4d76-a332-9819543040df?utm_source=share-modal&utm_medium=product-shared-content&utm_campaign=notebook&utm_content=6017cecd-c0c5-4d76-a332-9819543040df/README.md)

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

### チーム謝罪工房
