from flask import Flask, render_template
from flask_restful import reqparse, abort, Api, Resource


app = Flask(__name__)
api = Api(app)


class RecordDriverConfig(Resource):
    def get(self, config):
        pass



@app.route("/")
def hello_world():
    return "Hello World!"


api.add_resource(RecordDriverConfig, "/uploadconfig/<config>")
if __name__ == "__main__":
    app.debug = True
    app.run()