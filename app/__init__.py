from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_marshmallow import Marshmallow
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_jwt_simple import JWTManager

app = Flask(__name__)
app.config.from_object("config")
app.config["SECRET_KEY"] = "GUESS"
app.config["JWT_SECRET_KEY"] = "TOP-Secret"
api = Api(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)
login_manager = LoginManager()
bootstrap = Bootstrap(app)
jwt = JWTManager(app)


from app import modules, views
db.create_all()