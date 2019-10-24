from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
 
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['WTF_CSRF_SECRET_KEY'] = 'Erq8CGA2eSmwFJkFTJTYBbJWhfMPNOwG'
app.config['LDAP_PROVIDER_URL'] = 'ldap://ldap.forumsys.com:389/'
app.config['LDAP_PROTOCOL_VERSION'] = 3
db = SQLAlchemy(app)
 
app.secret_key = 'some_random_key'
 
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
 
from flask_ldap_login.auth.views import auth
app.register_blueprint(auth)
 
db.create_all()