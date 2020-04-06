from flask import request
from flask_restplus import Resource
from app.services import userService
from app.api.models import users_namespace, user_model, bids_model, bids_model_body



@users_namespace.route('')
class User(Resource):

    @users_namespace.marshal_list_with(user_model, skip_none=True)
    def get(self):
        try:
            users = userService.list_users()
            return users, 200 
        except Exception as e:
            users_namespace.abort(400, str(e))

    @users_namespace.marshal_with(user_model, skip_none=True)
    @users_namespace.expect(user_model)
    def post(self):
        try:
            user_dict = request.json.get("date") or request.json 
            user = userService.add_user(user_dict)
            return user, 200 
        except Exception as e:
            users_namespace.abort(400, str(e))



@users_namespace.route('/bids/<owner_id>/<pet_id>')
class UserBids(Resource):
    @users_namespace.marshal_list_with(bids_model, skip_none=True)
    def get(self, pet_id, owner_id):
        try:
            bids = userService.list_user_bids(pet_id, owner_id)
            return bids, 200 
        except Exception as e: 
            users_namespace.abort(400, str(e))


@users_namespace.route('/<user_id>/bid/<pet_id>')
class BidPet(Resource):
    @users_namespace.expect(bids_model_body)
    @users_namespace.marshal_list_with(bids_model, skip_none=True)
    def post(self, pet_id, user_id):
        try:
            bid_info = request.json.get("date") or request.json 
            bid_info.update({'pet_id':pet_id, 'user_id':user_id})
            bids = userService.bid_on_pet(bid_info)
            return bids, 200 
        except Exception as e:
            users_namespace.abort(400, str(e))
