from app.__init__ import db


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
        self.project = configfile["project"]
        self.devicename = configfile["devicename"]
        self.drivername = configfile["drivername"]
        self.path = configfile["path"]
        self.inffile = configfile["inffile"]
        self.version = configfile["version"]
        self.unzip = configfile["unzip"]
        self.unzippar = configfile["unzippar"]
        self.installmethod = configfile["installmethod"]
        self.installpar = configfile["installpar"]
        self.did = configfile["did"]
        self.vid = configfile["vid"]
        self.date = configfile["date"]

