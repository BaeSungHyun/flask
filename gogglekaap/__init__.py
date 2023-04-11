from flask import Flask
from flask import render_template
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

db = "database"

def create_app():
    app = Flask(__name__)

    # 원래는 wtf에서 해줘야 하는데, flask secretkey에서 해줘도 된다고 함
    app.config["SECRET_KEY"] = "secretkey"

    # static file cache하지 않고 바로 갱신
    if app.config["DEBUG"]:
        app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 1 

    ''' === CSRF Init === '''
    csrf.init_app(app) # I think this initializes csrf

    ''' === Routes Init === ''' # bluprint로 해줬어도 init.py에서 다시 한번 연결해야함
    from gogglekaap.routes import base_route, auth_route
    app.register_blueprint(base_route.bp)
    app.register_blueprint(auth_route.bp)

    @app.errorhandler(404)
    def page_404(error):
        return render_template("404.html"), 404
    
    return app