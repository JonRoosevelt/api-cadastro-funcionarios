from django.test import TestCase
from rest_framework.test import APIClient

from core.factories import NaverFactory, UserFactory


class NaverFilterByNameTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.naver_1 = NaverFactory(
            name='Rodrigo',
            created_by=cls.user
        )
        cls.naver_2 = NaverFactory(
            name='Marcela',
            created_by=cls.user
        )

    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.url = '/api/navers/'

    def test_project_filters_by_name_rodrigo(self):
        response = self.client.get(self.url, {'name': 'Rodrigo'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Rodrigo')

    def test_project_filters_by_name_marcela(self):
        response = self.client.get(self.url, {'name': 'Marcela'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Marcela')
