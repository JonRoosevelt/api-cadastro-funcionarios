import json

from django.test import TestCase
from rest_framework.test import APIClient

from core.factories import NaverProjetoFactory, UserFactory, ProjetoFactory


class ProjetoShowViewTestCase(TestCase):
    maxDiff = None

    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.projeto = ProjetoFactory(
            name='Projeto 1',
            created_by=cls.user
        )
        cls.naver_projetos = dict(
            naver_1=NaverProjetoFactory(
                projeto=cls.projeto,
                naver__name='José Souza',
                naver__birthdate='1991-02-01',
                naver__admission_date='2019-03-01',
                naver__job_role='Desenvolvedor BackEnd',
                naver__created_by=cls.user
            ),
            naver_2=NaverProjetoFactory(
                projeto=cls.projeto,
                naver__name='Maria Fernanda',
                naver__birthdate='1993-01-08',
                naver__admission_date='2019-04-02',
                naver__job_role='Desenvolvedor FrontEnd',
                naver__created_by=cls.user
            ),
            naver_3=NaverProjetoFactory(
                projeto=cls.projeto,
                naver__name='Marina Alves',
                naver__birthdate='1989-01-01',
                naver__admission_date='2018-05-07',
                naver__job_role='Tester',
                naver__created_by=cls.user
            ),
            naver_4=NaverProjetoFactory(
                projeto=cls.projeto,
                naver__name='Magno Oliveira',
                naver__birthdate='1994-10-02',
                naver__admission_date='2020-05-01',
                naver__job_role='Gerente de Projetos',
                naver__created_by=cls.user
            )
        )

        cls.expected_naver_show_response = dict(
            id=1,
            name='Projeto 1',
            navers=[
                dict(
                    id=1,
                    name='José Souza',
                    birthdate='1991-02-01',
                    admission_date='2019-03-01',
                    job_role='Desenvolvedor BackEnd'
                ),
                dict(
                    id=2,
                    name='Maria Fernanda',
                    birthdate='1993-01-08',
                    admission_date='2019-04-02',
                    job_role='Desenvolvedor FrontEnd'
                ),
                dict(
                    id=3,
                    name='Marina Alves',
                    birthdate='1989-01-01',
                    admission_date='2018-05-07',
                    job_role='Tester'
                ),
                dict(
                    id=4,
                    name='Magno Oliveira',
                    birthdate='1994-10-02',
                    admission_date='2020-05-01',
                    job_role='Gerente de Projetos'
                ),
            ]
        )

    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.url = f'/api/projetos/{self.projeto.id}/'

    def test_show_view_returns_projeto_detail_as_expected(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            json.dumps(response.data),
            json.dumps(self.expected_naver_show_response)
        )

    def test_assert_num_queries_equal_2(self):
        with self.assertNumQueries(2):
            self.client.get(self.url)
