# #@title　#5.Flask-SQLAlcyemyをアプリに設定をする

# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import DeclarativeBase

# class Base(DeclarativeBase):
#   pass #これは何にもしないと言う意味

# # SQLAlchemyをインスタンス化
# db = SQLAlchemy(model_class=Base)

# # SQLiteデータベースをappに設定する
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sample_db.sqlite"
# #  appを拡張とともに初期化
# db.init_app(app)