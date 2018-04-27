from flask_restful import reqparse, Resource
from app.modules import Configfile
from app import db, api, ma
from flask import jsonify

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
        return configfile_schema.dump(result).data, 200


class ConfigfileSchema(ma.ModelSchema):
    class Meta:
        model = Configfile


api.add_resource(DriverConfiginfo, "/configinfo/")