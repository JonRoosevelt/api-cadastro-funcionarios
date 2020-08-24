from django.test import TestCase
from rest_framework.test import APIClient

from core.factories import ProjetoFactory, UserFactory


class ProjectFilterByNameTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.project_1 = ProjetoFactory(
            name='projeto 1',
            created_by=cls.user
        )
        cls.project_2 = ProjetoFactory(
            name='projeto 2',
            created_by=cls.user
        )

    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.url = '/api/projetos/'

    def test_project_filters_by_name_projeto_1(self):
        response = self.client.get(self.url, {'name': 'projeto 1'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'projeto 1')

    def test_project_filters_by_name_projeto_2(self):
        response = self.client.get(self.url, {'name': 'projeto 2'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'projeto 2')
