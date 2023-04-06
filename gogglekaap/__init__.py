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

    ''' === auth === '''
    from gogglekaap.forms.auth_form import LoginForm, RegisterForm
    @app.route('/auth/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            user_id = form.user_id.data
            password = form.password.data
            return f"{user_id}, {password}"
        
        return render_template(
            "login.html", form=form
        )
    
    @app.route("/auth/logout")
    def logout():
        return "logout"
    
    @app.route('/auth/register', methods=['GET', 'POST'])
    def register():
        form = RegisterForm()
        if form.validate_on_submit():
            user_id = form.user_id.data
            user_name = form.user_name.data
            password = form.password.data
            repassword = form.repassword.data
            return f"{user_id}, {user_name}, {password}, {repassword}"
        return render_template('register.html', form=form)

    @app.route("/")
    def index():
        return render_template("index.html")
    
    @app.errorhandler(404)
    def page_404(error):
        return render_template("404.html"), 404
    
    return app