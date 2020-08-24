from django.test import TestCase
from rest_framework.test import APIClient

from core.factories import UserFactory, NaverFactory


class NaversUpdateViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.naver = NaverFactory(
            name='Joao Augusto',
            birthdate='1990-10-12',
            admission_date='2018-01-02',
            job_role='Desenvolvedor React',
            created_by=cls.user
        )
        cls.naver_new_data = dict(
            name='João Augusto Oliveira',
            birthdate='1991-10-12',
            admission_date='2018-01-03',
            job_role='Desenvolvedor FrontEnd',
            created_by=cls.user
        )

    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.url = '/api/navers/{}/'

    def test_updating_own_navers_works(self):
        response = self.client.put(
            self.url.format(self.naver.id), data=self.naver_new_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['id'], self.naver.id)
        self.assertEqual(
            response.data['name'], self.naver_new_data['name'])
        self.assertEqual(
            response.data['birthdate'],
            self.naver_new_data['birthdate'])
        self.assertEqual(
            response.data['admission_date'],
            self.naver_new_data['admission_date'])
        self.assertEqual(
            response.data['job_role'],
            self.naver_new_data['job_role'])