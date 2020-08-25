from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from core.models import User


class JwtAuthTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_credentials = dict(
            email='user@navedex.tk',
            password='user123'
        )

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            self.user_credentials['email'], self.user_credentials['password'])

    def test_login(self):
        response = self.client.post(
            '/auth/login/', 
            data=self.user_credentials, 
            format='json')
        self.assertEqual(response.status_code, 200)