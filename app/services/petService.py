from app.app_creator import db
from app.models import Pet, model_from_dict
 
def create_dummy_pet(petname, owner_id=None):
    return{
        'name': petname,
        'owner_id':owner_id,
        'status':'available'
    }

def add_pet (pet_dict):
    pet = Pet()
    model_from_dict(pet, **pet_dict)
    db.session.add(pet)
    db.session.commit()
    return pet

def list_pets():
    res = db.session.query(Pet).all()
    return res

def list_user_pets(user_id):
    res = db.session.query(Pet).filter(Pet.owner_id == user_id).all()
    return res

def get_pet(pet_id):
    return db.session.query(Pet).filter(Pet.id == pet_id).one()