from flask import Flask, render_template
from flask_restful import reqparse, abort, Api, Resource
from flask_sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)
app.config.from_object("config")
api = Api(app)
db = SQLAlchemy(app)
db.create_all()

class RecordDriverConfig(Resource):
    def get(self, config):
        return "config:{0}".format(config)



#@app.route("/")
#def hello_world():
#    return "Hello World!"


api.add_resource(RecordDriverConfig, "/uploadconfig/<config>")
if __name__ == "__main__":
    app.debug = True
    app.run()