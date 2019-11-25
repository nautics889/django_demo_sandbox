from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

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
    client = APIClient()
    token = 'test123455'

    @classmethod
    def setUpTestData(cls):
        cls.user = factories.SandyUserFactory.create()
        cls.user.set_password(cls.user.password)
        cls.user.save()
        cls.user.oauth2_provider_accesstoken.create(
            expires='2050-12-31 23:59:59', token=cls.token
        )
        import pdb
        pdb.set_trace()

    def setUp(self):
        self.url = reverse('retrive-details-current-user')
        # TODO: make more correct user creation (via factory's method)
        self.client.credentials(Authorization='Bearer {}'.format(self.token))

    def test_ensure_current_user(self):
        import pdb
        pdb.set_trace()
        pass
        # response = self.client.get(self.url)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.body)
