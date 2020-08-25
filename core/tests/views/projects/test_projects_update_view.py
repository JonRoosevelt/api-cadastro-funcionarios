from django.test import TestCase
from rest_framework.test import APIClient

from core.factories import ProjetoFactory, UserFactory


class ProjectsUpdateViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.other_user = UserFactory()
        cls.own_project = ProjetoFactory(
            name='Projeto 1',
            created_by=cls.user
        )
        cls.others_project = ProjetoFactory(
            name='Projeto 2',
            created_by=cls.other_user
        )

        cls.own_project_new_data = dict(
            name='Projeto 1 alterado',
            created_by=cls.user
        )

        cls.others_project_new_data = dict(
            name='Projeto 2 alterado',
            created_by=cls.other_user
        )

    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.url = '/api/projetos/{}/'

    def test_updating_own_navers_works(self):
        response = self.client.put(
            self.url.format(self.own_project.id), data=self.own_project_new_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['id'], self.own_project.id)
        self.assertEqual(response.data['name'], self.own_project_new_data['name'])

    def test_updating_others_project_returns_403(self):
        response = self.client.put(
            self.url.format(
                self.others_project.id),
            data=self.others_project_new_data
        )
        self.assertEqual(response.status_code, 403)
    
    def test_updating_non_existent_project_returns_404(self):
        response = self.client.put(
            self.url.format(5),
            data=self.others_project_new_data
        )
        self.assertEqual(response.status_code, 404)