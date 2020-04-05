from flask_restplus import Namespace, fields, reqparse

bids_namespace = Namespace("Bids")
users_namespace = Namespace("Users")
pets_namespace = Namespace("Pets")

tag_model = pets_namespace.model('Tag', {
    "id": fields.Integer,
    "name": fields.String,
})

category_model = pets_namespace.model('Category', {
    "id": fields.Integer,
    "name": fields.String,
})

user_model = users_namespace.model('User', {
    "id": fields.Integer,
    "username": fields.String,
    "firstname": fields.String,
    "lastname": fields.String,
    "email": fields.String,
    "phone": fields.String,
    "userstatus": fields.Integer,
})

pet_model = pets_namespace.model('Pet', {
   "id": fields.Integer,
   "owner": fields.Nested(user_model, skip_none=True),
   "name": fields.String,
   "status": fields.String,
   "tags":fields.List(fields.Nested(tag_model, skip_none=True)),
   "category":fields.Nested(category_model, skip_none=True)

})

bids_model = users_namespace.model('Bid', {
   "id": fields.Integer,
   "pet_id": fields.Integer,
   "user_id": fields.Integer,
   "amount": fields.Float,
   "pet": fields.Nested(pet_model, skip_none=True),
   "user": fields.Nested(user_model, skip_none=True),
})

bids_model_body = users_namespace.model('BidBody', {
    "amount": fields.Float,
})
