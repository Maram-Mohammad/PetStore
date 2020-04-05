from app.app_creator import db

class Pet(db.Model):
    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship("Category")

    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    owner = db.relationship("User", lazy="select")

    name = db.Column(db.String, nullable=False)
    photo_urls = db.Column(db.Text, nullable=True)
    status = db.Column(db.Enum('available', 'pending', 'sold', name='pet_state'), nullable=False)
    tags = db.relationship("PetTag", back_populates="pet", lazy='joined')
    

class PetTag(db.Model):
    __tablename__ = "pet_tag"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pet_id = db.Column(db.Integer, db.ForeignKey('pets.id'))
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'))
    tag = db.relationship("Tag", lazy='select')
    pet = db.relationship("Pet", back_populates="tags", lazy='select')
