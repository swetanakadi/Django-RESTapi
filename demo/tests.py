import json

from rest_framework import status
from rest_framework.test import APITestCase
from .models import Drink
from django.urls import reverse


# Create your tests here.

class DrinkTestCase(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('drink_list')
        self.instance = Drink.objects.create(name='mojito')
        self.valid_data = {
            'name': 'Cappuccino'
        }
        self.invalid_data = {
            'name': 'mojito'
        }

    def test_valid_drink(self):
        response = self.client.post(self.url, data=json.dumps(self.valid_data), content_type='application/json')
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_drink(self):
        response = self.client.post(self.url, data=json.dumps(self.invalid_data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
