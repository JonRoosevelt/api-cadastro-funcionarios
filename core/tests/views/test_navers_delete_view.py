from django.test import TestCase
from rest_framework.test import APIClient

from core.factories import UserFactory, NaverFactory


class NaversDeleteViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.other_user = UserFactory()
        cls.own_naver = NaverFactory(
            name='Joao Augusto',
            birthdate='1990-10-12',
            admission_date='2018-01-02',
            job_role='Desenvolvedor React',
            created_by=cls.user
        )
        cls.others_naver = NaverFactory(
            created_by=cls.other_user
        )

    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.url = '/api/navers/{}/'

    def test_deleting_own_navtest_deleting_own_navers_returns_204(self):
        response = self.client.delete(self.url.format(self.own_naver.id))
        self.assertEqual(response.status_code, 204)

    def test_deleting_others_navers_returns_403(self):
        response = self.client.delete(self.url.format(self.others_naver.id))
        self.assertEqual(response.status_code, 403)

    def test_deleting_non_existent_naver_returns_404(self):
        response = self.client.delete(self.url.format(4))
        self.assertEqual(response.status_code, 404)
