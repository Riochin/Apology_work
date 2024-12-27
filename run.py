from app import create_app
from app.database import initialize_books_data, create_books_table

print("Hello, World!")
app = create_app()
print("app:", app)

# データベースを初期化
create_books_table()

initialize_books_data()
print("データベースの初期化が完了しました。")

if __name__ == "__main__": #Python3では、__name__が__main__になる
    # アプリケーションを起動
    print("アプリケーションを起動します。")
    app.run(debug=True, host='127.0.0.1',port=5000)
    print("アプリケーションを起動しました。")

    # テーブル作成
    # create_books_table()

    

    

    
