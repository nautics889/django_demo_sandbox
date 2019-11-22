from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from user_app.tests import factories
from user_app.models import SandyUser


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


class SandyCurrentUserDetailsTest(APITestCase):
    def setUp(self):
        self.url = reverse('retrive-details-current-user')
        user_instance = factories.SandyUserFactory.build()
        # TODO: make more correct user creation (via factory's method)
        SandyUser.objects.create_user(username=user_instance.username,
                                      email=user_instance.email,
                                      password=user_instance.password)
        self.data = dict(username=user_instance.username,
                         email=user_instance.email,
                         password=user_instance.password)
        self.client.login()
        self.client.login(username=user_instance.username,
                          password=user_instance.password)

    def test_ensure_current_user(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.body)
