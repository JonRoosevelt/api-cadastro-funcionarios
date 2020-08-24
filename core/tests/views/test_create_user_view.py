from django.test import TestCase
from rest_framework.test import APIClient

from core.models import User


class CreateUserViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/users/register'

    def test_if_user_can_register_using_email_and_password(self):
        response = self.client.post(
            self.url, data={'email': 'johndoe@doe.com', 'password': 'xKv2@123'})
        users = User.objects.all()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].email, 'johndoe@doe.com')
