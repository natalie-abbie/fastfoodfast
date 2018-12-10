import unittest
from fastfoodsapp import app
from flask import json

class food(unittest.TestCase):
   client = app.test_client()
   user = {
               "username":"jenny",
               "password":"password",
               "role":"admin"
           }

   def test_register_successfully(self):
       
       response = self.client.post('/api/v1/register', data=json.dumps(self.user), content_type='application/json')
       data = json.loads(response.data.decode())
       print(data)
       self.assertEqual('Account created successfully', data['message'])
       self.assertEqual(201, response.status_code)

   def test_username_missing(self):
       user2 = self.user
       del user2['username']
       response = self.client.post('/api/v1/register', data=json.dumps(user2), content_type='application/json')
       data = json.loads(response.data.decode())
       self.assertEqual("username can't be blank", data['message'])
       self.assertEqual(400, response.status_code)


if __name__ == '__main__':
   unittest.main()