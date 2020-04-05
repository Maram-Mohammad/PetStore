
#!/usr/bin/env python
"""
App initializaer, loaded once in the lifetime of the app (everytime the webservers restarts),
but can run inside multiple processes if webserver has multiple workers
Contains all initialization code
Note that we do not use an static vars or long living cache objects yet, because these are tricky.
"""
# pylint: disable=ungrouped-imports,wrong-import-order
from app.config import app_settings
from flask_migrate import Migrate
from .app_creator import create_app, db
from .models import *
from flask_swagger_ui import get_swaggerui_blueprint 

app = create_app(__name__)
migrate = Migrate(app, db)

from .api import api_namespaces 


SWAGGER_DOCS_URL = '/api/docs' 
swaggerui_blueprint = get_swaggerui_blueprint(
    base_url=SWAGGER_DOCS_URL,
    config=dict(
        app_name='API Reference', layout='BaseLayout',
        defaultModelsExpandDepth=1,
        docExpansion='none', 
    ),
    api_url='/api/swagger.json'
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_DOCS_URL)
app.config.update(SWAGGER_SUPPORTED_SUBMIT_METHODS=["get", "post"])
app.config.update(RESTPLUS_MASK_SWAGGER=False)


rest_api = api_namespaces(app=app, prefix='/api', doc=False, title='Pets Store Api')



@app.route("/")
def hello_world():
    try:
        from app.services import userService, petService
        user_1 = userService.add_user(userService.create_dummy_user('user1'))
        user_2 = userService.add_user(userService.create_dummy_user('user2'))
        user_3 = userService.add_user(userService.create_dummy_user('user3'))
        pet = petService.add_pet(petService.create_dummy_pet("pet1", user_1.id))
        return "app is successed up >>>> user records ids {} {} {} pushed into db >>>> and pet {} id pushed as well. >> userid {} is owner of pet id {}".format(user_1.id, user_2.id, user_3.id, pet.id, user_1.id, pet.id), 200
    except Exception as e:
        print(">>>>>>>>>>>>>>>>>>>>>> E >>>>>>>>>> ", str(e))
        return str(e), 400



