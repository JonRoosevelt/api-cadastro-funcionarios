from django.test import TestCase
from rest_framework.test import APIClient

from core.factories import ProjetoFactory, UserFactory


class ProjetoFactoryViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.other_user = UserFactory()
        cls.own_project = ProjetoFactory(
            created_by=cls.user
        )
        cls.others_project = ProjetoFactory(
            created_by=cls.other_user
        )

    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.url = '/api/projetos/{}/'

    def test_deleting_own_project_returns_204(self):
        response = self.client.delete(self.url.format(self.own_project.id))
        self.assertEqual(response.status_code, 204)

    def test_deleting_others_project_returns_403(self):
        response = self.client.delete(self.url.format(self.others_project.id))
        self.assertEqual(response.status_code, 403)

    def test_deleting_non_existent_project_returns_404(self):
        response = self.client.delete(self.url.format(4))
        self.assertEqual(response.status_code, 404)
