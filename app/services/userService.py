from app.app_creator import db
from app.models import Bid, Pet, User, model_from_dict
from sqlalchemy import and_
from app.services.petService import get_pet
def create_dummy_user(username):
    return{
        'email':username,
        'username':username,
        'password':username
    }

def add_user (user_dict):
    user = User()
    model_from_dict(user, **user_dict)
    db.session.add(user)
    db.session.commit()
    return user

def list_users():
    res = db.session.query(User).all()
    return res




def is_pet_owner(pet_id, owner_id):
    res = db.session.query(Pet).filter(and_(Pet.id == pet_id, Pet.owner_id == owner_id)).first()
    if res:
        return True
    return False


def list_user_bids(pet_id, owner_id):
    get_user(owner_id)
    get_pet(pet_id)
    if is_pet_owner(pet_id, owner_id):
        res = db.session.query(Bid).filter(Bid.pet_id == pet_id).all()
        return res

    raise Exception("Request forbbiden, this user is not allowed to access requested data")
    
def bid_on_pet(bid_info):
    user_id = bid_info.get("user_id")
    pet_id = bid_info.get("pet_id")
    get_user(user_id)
    get_pet(pet_id)

    if not is_pet_owner(pet_id, user_id):
        bid = Bid()
        model_from_dict(bid, **bid_info)
        db.session.add(bid)
        db.session.commit()
        return bid
    
    raise Exception("Request forbbiden, pet owner couldn't join the Bid")

def get_user(user_id):
    return db.session.query(User).filter(User.id == user_id).one()

