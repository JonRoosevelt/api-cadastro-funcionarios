import json

from django.test import TestCase
from rest_framework.test import APIClient


from core.factories import UserFactory, ProjetoFactory


class ProjectsIndexViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.projetos_dict = dict(
            projeto_1=ProjetoFactory(
                name='Projeto 1',
                created_by=cls.user
            ),
            projeto_2=ProjetoFactory(
                name='Projeto 2',
                created_by=cls.user
            )
        )

        cls.expected_projects_list = [
            dict(
                id=1,
                name='Projeto 1'
            ),
            dict(
                id=2,
                name='Projeto 2'
            ),
        ]

    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.url = '/api/projetos/'

    def test_index_view_returns_projects_list_as_expected(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            json.dumps(response.data),
            json.dumps(self.expected_projects_list)
        )