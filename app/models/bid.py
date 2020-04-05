from app.app_creator import db

class Bid(db.Model):
    __tablename__ = "pet_bids"
 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pet_id = db.Column(db.Integer, db.ForeignKey('pets.id'))
    amount = db.Column(db.Float, nullable=False, default=0.0)
    user = db.relationship("User", lazy='select')
    pet = db.relationship("Pet", lazy='select')

