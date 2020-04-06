from flask_restplus import Resource
from flask import request
from app.services import petService
from app.api.models import pets_namespace, pet_model



@pets_namespace.route('')
class Pet(Resource):

    @pets_namespace.marshal_list_with(pet_model, skip_none=True)
    def get(self):
        try:
            pets = petService.list_pets()
            return pets, 200 
        except Exception as e:
            pets_namespace.abort(400, str(e))
    
    @pets_namespace.marshal_list_with(pet_model, skip_none=True)
    @pets_namespace.expect(pet_model)
    def post(self):
        try:
            pet_dict = request.json.get("date") or request.json 
            pet = petService.add_pet(pet_dict)
            return pet, 200 
        except Exception as e:
            pets_namespace.abort(400, str(e))
   
    

@pets_namespace.route('/<user_id>')
class UserPets(Resource):

    @pets_namespace.marshal_list_with(pet_model, skip_none=True)
    def get(self, user_id):
        try:
            pets = petService.list_user_pets(user_id)
            return pets, 200 
        except Exception as e:
            pets_namespace.abort(400,str(e))
