from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from user_app.tests import factories


class SandyCurrentUserDetailsTest(APITestCase):
    client = APIClient()
    token = 'test12345'

    @classmethod
    def setUpTestData(cls):
        cls.user = factories.SandyUserFactory.create()
        cls.user.set_password(cls.user.password)
        cls.user.save()
        token = cls.user.oauth2_provider_accesstoken.create(
            expires='2050-12-31 23:59:59', token=cls.token
        )
        token.scope = 'read write'
        token.save()

    def setUp(self):
        self.url = reverse('retrive-details-current-user')
        self.client.credentials(Authorization='Bearer {}'.format(self.token))

    def test_current_user_info(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)
        self.assertEqual(response.data['email'], self.user.email)
