import json

from django.test import TestCase
from rest_framework.test import APIClient

from core.models import Projeto
from core.factories import UserFactory


class ProjectsStoreViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory(
            email='gerente@navedex.nv',
        )
        cls.project = dict(
            name='Projeto 1',
        )

    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.url = '/api/projetos/'

    def test_store_view_creates_new_project(self):
        response = self.client.post(self.url, data=self.project)
        projeto = Projeto.objects.all()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(projeto), 1)
        self.assertEqual(
            json.dumps(response.data['name']),
            json.dumps(self.project['name'])
        )
