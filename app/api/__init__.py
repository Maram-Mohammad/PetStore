from flask_restplus import Api
from .pet_api import pets_namespace
from .user_api import users_namespace

def api_namespaces(**kwargs):
    rest_plus_api = Api(**kwargs)
    rest_plus_api.add_namespace(users_namespace, path="/users")
    rest_plus_api.add_namespace(pets_namespace, path="/pets")
    
    return rest_plus_api