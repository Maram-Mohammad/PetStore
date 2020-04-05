from app.app_creator import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False)
    firstname = db.Column(db.String, nullable=True)
    lastname = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=False)
    password =  db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=True)
    userstatus =  db.Column(db.Integer, nullable=True)

