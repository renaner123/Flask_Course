from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '65611608a47ff8feafd3774a'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page" #informa ao método do flask_login login_required a onde preicsa encaminhar o pedido de login
login_manager.login_message_category = "info" #por padrão, login_required não tem categoria
from market import routes
from market import models