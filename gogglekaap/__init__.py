from flask import Flask
from flask import render_template

db = "database"

def create_app():
    app = Flask(__name__)

    # static file cache하지 않고 바로 갱신
    if app.config["DEBUG"]:
        app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 1 

    @app.route("/")
    def index():
        return render_template("index.html")
    
    @app.errorhandler(404)
    def page_404(error):
        return render_template("404.html"), 404
    
    return app