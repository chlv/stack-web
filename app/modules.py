from app import db


class Configfile(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    project = db.Column(db.String(120))
    devicename = db.Column(db.String(64))
    drivername = db.Column(db.String(120))
    path = db.Column(db.String(120))
    inffile = db.Column(db.String(64))
    version = db.Column(db.String(64))
    unzip = db.Column(db.String(64))
    unzippar = db.Column(db.String(64))
    installmethod = db.Column(db.String(64))
    installpar = db.Column(db.String(120))
    did = db.Column(db.String(64))
    vid = db.Column(db.String(64))
    date = db.Column(db.String(64))

    def __init__(self, configfile):
        self.project = configfile["Project"]
        self.devicename = configfile["DeviceName"]
        self.drivername = configfile["DriverName"]
        self.path = configfile["PATH"]
        self.inffile = configfile["inffile"]
        self.version = configfile["Version"]
        self.unzip = configfile["Unzip"]
        self.unzippar = configfile["UnzipPar"]
        self.installmethod = configfile["InstallMethod"]
        self.installpar = configfile["InstallPar"]
        self.did = configfile["DID"]
        self.vid = configfile["VID"]
        self.date = configfile["Date"]


class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(64))
    password = db.Column(db.String(128))
    email = db.Column(db.String(64))

    def __init__(self, userinfo):
        self.name = userinfo["name"]
        self.password = userinfo["password"]
        self.email = userinfo["email"]
