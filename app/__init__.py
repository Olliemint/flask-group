from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_login import LoginManager



app = Flask(__name__)
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'


login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

from app.main import views
