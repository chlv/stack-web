from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
app.config.from_object("config")
api = Api(app)
db = SQLAlchemy(app)

from app import modules, views
db.create_all()