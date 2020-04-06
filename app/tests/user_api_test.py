import unittest
import sqlalchemy
import json
from app import app
from app.app_creator import db
from app.services import petService, userService

USER_LIST_BIDS_API_PATH = 'api/users/bids/{owner_id}/{pet_id}'
USER_BID_API_PATH = 'api/users/{user_id}/bid/{pet_id}'

class TestBidsApi(unittest.TestCase):

    def setUp(self):
        with app.app_context():
            url = "postgresql://adminuser:adminpass@localhost/petsdb.test"
            app.config['TESTING'] = True
            app.config['SQLALCHEMY_DATABASE_URI'] = url
            self.engine = sqlalchemy.create_engine(url)
            db.create_all()
            self.client = app.test_client()
            
    def tearDown(self):
        with app.app_context():
            db.session.close()
            db.session.remove()
            db.drop_all()

    def set_data_into_db(self):
        user_1 = userService.add_user(userService.create_dummy_user("user1"))
        user_2 = userService.add_user(userService.create_dummy_user("user2"))
        user_3 = userService.add_user(userService.create_dummy_user("user3"))
        pet = petService.add_pet(petService.create_dummy_pet("cat", user_1.id))
        return user_1, user_2, user_3, pet
        

    def test_bid_on_pet(self):
        with app.app_context(), self.client:
            info = self.set_data_into_db()
            headers = {
                "Content-Type": "application/json"
            }
            req_body = {
                "amount":6
            }
            response = self.client.post(USER_BID_API_PATH.format(user_id=info[1].id, pet_id=info[3].id), headers=headers, json=req_body)
            self.assertEqual(response.status_code, 200, response.data)
            


    def test_list_user_bids(self):
        with app.app_context(), self.client:
            info = self.set_data_into_db()
            headers = {
                "Content-Type": "application/json"
            }
            req_body = {
                "amount":6
            }
            response = self.client.post(USER_BID_API_PATH.format(user_id=info[1].id, pet_id=info[3].id), headers=headers, json=req_body)
            self.assertEqual(response.status_code, 200, response.data)
            
            response = self.client.post(USER_BID_API_PATH.format(user_id=info[2].id, pet_id=info[3].id), headers=headers, json=req_body)
            self.assertEqual(response.status_code, 200, response.data)
            
            response = self.client.get(USER_LIST_BIDS_API_PATH.format(owner_id=info[0].id, pet_id=info[3].id))
            self.assertEqual(response.status_code, 200, response.data)
            data = json.loads(response.data)
            self.assertEqual(len(data), 2, response.data)
            

    def test_owner_bids_on_his_pet(self):
        with app.app_context(), self.client:
            info = self.set_data_into_db()
            headers = {
                "Content-Type": "application/json"
            }
            req_body = {
                "amount":6
            }
            response = self.client.post(USER_BID_API_PATH.format(user_id=info[0].id, pet_id=info[3].id), headers=headers, json=req_body)
            self.assertEqual(response.status_code, 400, response.data)
            


    def test_list_user_bids_not_owner(self):
        with app.app_context(), self.client:
            info = self.set_data_into_db()
            headers = {
                "Content-Type": "application/json"
            }
            req_body = {
                "amount":6
            }
            response = self.client.post(USER_BID_API_PATH.format(user_id=info[1].id, pet_id=info[3].id), headers=headers, json=req_body)
            self.assertEqual(response.status_code, 200, response.data)
            
            response = self.client.post(USER_BID_API_PATH.format(user_id=info[2].id, pet_id=info[3].id), headers=headers, json=req_body)
            self.assertEqual(response.status_code, 200, response.data)
            
            response = self.client.get(USER_LIST_BIDS_API_PATH.format(owner_id=info[1].id, pet_id=info[3].id))
            self.assertEqual(response.status_code, 400, response.data)
        
            
if __name__ == '__main__':
      unittest.main()