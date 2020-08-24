import json

from django.test import TestCase
from rest_framework.test import APIClient

from core.factories import NaverFactory, NaverProjetoFactory, UserFactory


class NaversShowViewTestCase(TestCase):
    maxDiff = None

    @classmethod
    def setUpTestData(cls):
        cls.naver = NaverFactory(
            name='Joao Augusto',
            birthdate='1990-10-12',
            admission_date='2018-01-02',
            job_role='Desenvolvedor React',
        )
        cls.naver_projetos = dict(
            projeto_1=NaverProjetoFactory(
                projeto__name='Projeto 1',
                naver=cls.naver
            ),
            projeto_2=NaverProjetoFactory(
                projeto__name='Projeto 2',
                naver=cls.naver
            ),
            projeto_3=NaverProjetoFactory(
                projeto__name='Projeto 3',
                naver=cls.naver
            ),
            projeto_4=NaverProjetoFactory(
                projeto__name='Projeto 4',
                naver=cls.naver
            ),
        )

        cls.expected_naver_show_response = dict(
            id=1,
            name='Joao Augusto',
            birthdate='1990-10-12',
            admission_date='2018-01-02',
            job_role='Desenvolvedor React',
            projects=[
                dict(
                    id=1,
                    name='Projeto 1'
                ),
                dict(
                    id=2,
                    name='Projeto 2'
                ),
                dict(
                    id=3,
                    name='Projeto 3'
                ),
                dict(
                    id=4,
                    name='Projeto 4'
                ),
            ]
        )

    def setUp(self):
        self.user = UserFactory()
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.url = f'/api/navers/{self.naver.id}/'

    def test_show_view_returns_naver_detail_as_expected(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            json.dumps(response.data),
            json.dumps(self.expected_naver_show_response)
        )

    def test_assert_num_queries_equal_2(self):
        with self.assertNumQueries(2):
            self.client.get(self.url)
