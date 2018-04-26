from flask import Flask, render_template
from flask_restful import reqparse, abort, Api, Resource
from flask_sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)
app.config.from_object("config")
api = Api(app)
db = SQLAlchemy(app)
db.create_all()
parase = reqparse.RequestParser()

class DriverConfiginfo(Resource):
    def post(self):
        parase.add_argument("platform", type=str)
        args = parase.parse_args()
        task = {"platform": args["platform"]}
        print(task)
        return task, 201

    def get(self):
        return {"hello": "World1"}



#@app.route("/")
#def hello_world():
#    return "Hello World!"


api.add_resource(DriverConfiginfo, "/configinfo/")
if __name__ == "__main__":
    app.debug = True
    app.run(threaded=True)