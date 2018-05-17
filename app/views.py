from flask_restful import reqparse, Resource
from app.modules import Configfile, User
from app import db, api, ma
from flask import jsonify
from flask_jwt_simple import jwt_required, create_jwt, get_jwt_identity


parase = reqparse.RequestParser()


class DriverConfiginfo(Resource):
    def post(self):
        parase.add_argument("DriverName", type=str)
        parase.add_argument("DeviceName", type=str)
        parase.add_argument("Unzip", type=str)
        parase.add_argument("UnzipPar", type=str)
        parase.add_argument("PATH", type=str)
        parase.add_argument("InstallMethod", type=str)
        parase.add_argument("InstallPar", type=str)
        parase.add_argument("DID", type=str)
        parase.add_argument("VID", type=str)
        parase.add_argument("Version", type=str)
        parase.add_argument("Date", type=str)
        parase.add_argument("Project", type=str)
        parase.add_argument("inffile", type=str)
        args = parase.parse_args()
        for key in args.keys():
            if key == "Undefined":
                del args["Undefined"]
        configinfo = Configfile(args)
        db.session.add(configinfo)
        db.session.commit()
        return args, 201

    def get(self):
        configfile_schema = ConfigfileSchema(many=True)
        result = Configfile.query.all()
        output = configfile_schema.dump(result).data
        response = jsonify({"InfoItems": output})
        response.status_code = 200
        return response


class ConfigfileSchema(ma.ModelSchema):
    class Meta:
        model = Configfile

class UserSchema(ma.ModelSchema):
    class Meta:
        model = User


class Register(Resource):
    def post(self):
        parase.add_argument("name", type=str, required=True)
        parase.add_argument("password", type=str, required=True)
        parase.add_argument("email", type=str, required=True)
        args = parase.parse_args()
        email = args["email"]
        user_schema = UserSchema()
        result = User.query.filter_by(email=email).first()
        output = user_schema.dump(result).data
        print(output.keys())
        if not result:
            user = User(args)
            db.session.add(user)
            db.session.commit()
            return args, 201
        else:
            response = jsonify({"Error": "Email {0} have been used".format(email)})
            response.status_code = 400
            return response


class Login(Resource):
    def post(self):
        parase.add_argument("username", type=str, required=True)
        parase.add_argument("password", type=str, required=True)
        args = parase.parse_args()
        username = args["username"]
        password = args["password"]
        name_check = User.query.filter_by(name=username).first()
        password_check = User.query.filter_by(name=username, password=password).first()
        if name_check:
            if password_check:
                auth = True
                message = "Welcome {0}!".format(username)
            else:
                auth = False
                message = "{0},Please input correct password!".format(username)
        else:
            auth = False
            message = "{0} is not found, please sign in first!".format(username)
        if auth:
            token = {"jwt": create_jwt(identity=username)}
            response = jsonify(token)
            response.status_code = 200
            return response
        else:
            response = jsonify({"Error": message})
            response.status_code = 400
            return response



class Protected(Resource):
    @jwt_required
    def get(self):
        response = jsonify({"hello from": get_jwt_identity()})
        response.status_code = 200
        return response


api.add_resource(DriverConfiginfo, "/api/configinfo")
api.add_resource(Register, "/api/register")
api.add_resource(Login, "/api/login")
api.add_resource(Protected, "/api/protected")