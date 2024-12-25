from flask import render_template

def init_routes(app):
    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route("/about")
    def about():
        return "<h1>About Page</h1>"
