from flask_restplus import Resource
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
   
    

@pets_namespace.route('/<user_id>')
class UserPets(Resource):

    @pets_namespace.marshal_list_with(pet_model, skip_none=True)
    def get(self, user_id):
        try:
            pets = petService.list_user_pets(user_id)
            return pets, 200 
        except Exception as e:
            pets_namespace.abort(400,str(e))
