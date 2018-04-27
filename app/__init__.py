from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_marshmallow import Marshmallow
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object("config")
api = Api(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)
login_manager = LoginManager()




from app import modules, views
db.create_all()