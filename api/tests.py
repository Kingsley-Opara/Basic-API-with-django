from django.test import TestCase
import requests
from .models import Persons


# Create your tests here.
endpoint = 'https://api-person-service.onrender.com/api/'
class TestApiEndpoint(TestCase):
    # def setUp(self) :
    #     queryset = Persons.objects.all()
    #     self.assertIsNotNone(queryset.exists())
    #     return super().setUp()
    
    def test_list_endpoint(self):
        get_response = requests.get('https://api-person-service.onrender.com/api/list/', timeout=60)

        self.assertEqual(get_response.status_code, 200)

    def test_create_users_endpoint(self):
        data = {
            "name": "Martin",
            "email": "martin@yahoo.com",
            "nationality": "Nigrian",
            "state_of_origin": "Imo",
            "occupation": "student"
        }
        get_response = requests.post(endpoint, json=data, timeout=60)
        print(get_response.json())
        self.assertNotEqual(get_response.status_code, 200)
