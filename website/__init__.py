from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import  LoginManager

db = SQLAlchemy()
DB_NAME = "database1.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "Arianit's secret key "#encrypt/secure cookies and session data related to the website

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)



    #i importojme dhe i regjistrojme viewsat(blueprints)
    from website.routes.views import  views
    from website.routes.auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')#url_prefix tregon se si ti qasemi blueprintit te caktuar p.sh nese do ishte /auth/ atehere per tarritur te nje route hello duet te shkruajm /auth/hello

    from website.Models.models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'  # ku duhet te na dergoje nese sjemi loggedin
    login_manager.init_app(app)  # i tregon login managerit se cilin app perdorim

#se cilin user kerkojme
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')