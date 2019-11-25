from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from user_app.models import SandyUser
from user_app.tests import factories


class CreateSandyUserTest(APITestCase):
    def setUp(self):
        self.url = reverse('list-create-users')
        user_instance = factories.SandyUserFactory.build()
        self.data = dict(username=user_instance.username,
                         email=user_instance.email,
                         password=user_instance.password)

    def test_valid_data(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(SandyUser.objects.get(email=self.data['email']))
