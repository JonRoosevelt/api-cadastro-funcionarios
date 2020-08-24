from django.test import TestCase
from rest_framework.test import APIClient

from core.factories import NaverFactory, UserFactory


class NaversUpdateViewTestCase(TestCase):
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
        cls.naver_new_data = dict(
            name='João Augusto Oliveira',
            birthdate='1991-10-12',
            admission_date='2018-01-03',
            job_role='Desenvolvedor FrontEnd',
            created_by=cls.user
        )
        cls.others_naver = NaverFactory(
            created_by=cls.other_user
        )
        cls.others_naver_new_data = dict(
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
            self.url.format(self.own_naver.id), data=self.naver_new_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['id'], self.own_naver.id)
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

    def test_updating_others_navers_returns_403(self):
        response = self.client.put(
            self.url.format(
                self.others_naver.id),
            data=self.others_naver_new_data
        )
        self.assertEqual(response.status_code, 403)

    def test_updating_non_existent_naver_returns_404(self):
        response = self.client.put(
            self.url.format(5),
            data=self.others_naver_new_data
        )
        self.assertEqual(response.status_code, 404)
