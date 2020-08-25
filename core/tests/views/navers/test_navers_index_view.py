import json

from django.test import TestCase
from django.utils.dateparse import parse_date
from rest_framework.test import APIClient
from freezegun import freeze_time

from core.factories import NaverFactory, UserFactory


class NaversIndexViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory()
        cls.navers_dict = dict(
            naver_1=NaverFactory(
                name="Joao Augusto",
                birthdate=parse_date('1990-10-12'),
                admission_date=parse_date('2018-01-02'),
                job_role='Desenvolvedor React',
                created_by=cls.user
            ),
            naver_2=NaverFactory(
                name='Fernanda Oliveira',
                birthdate=parse_date('1995-08-06'),
                admission_date=parse_date('2019-05-03'),
                job_role='Desenvolvedora Backend',
                created_by=cls.user
            ),
            naver_3=NaverFactory(
                name='Deivison Pereira',
                birthdate=parse_date('1999-02-03'),
                admission_date=parse_date('2020-01-04'),
                job_role='Estagiário Teste',
                created_by=cls.user
            ),
            naver_4=NaverFactory(
                name='Priscila Marques',
                birthdate=parse_date('1987-01-23'),
                admission_date=parse_date('2014-02-02'),
                job_role='Gerente de Projetos',
                created_by=cls.user
            )
        )

        cls.expected_navers_list = [
            dict(
                id=1,
                name='Joao Augusto',
                birthdate='1990-10-12',
                admission_date='2018-01-02',
                job_role='Desenvolvedor React'
            ),
            dict(
                id=2,
                name='Fernanda Oliveira',
                birthdate='1995-08-06',
                admission_date='2019-05-03',
                job_role='Desenvolvedora Backend'
            ),
            dict(
                id=3,
                name='Deivison Pereira',
                birthdate='1999-02-03',
                admission_date='2020-01-04',
                job_role='Estagiário Teste'
            ),
            dict(
                id=4,
                name='Priscila Marques',
                birthdate='1987-01-23',
                admission_date='2014-02-02',
                job_role='Gerente de Projetos'
            )
        ]

    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.url = '/api/navers/'

    def test_index_view_returns_navers_list_as_expected(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            json.dumps(response.data),
            json.dumps(self.expected_navers_list)
        )

    def test_index_view_filter_by_name(self):
        naver_1 = self.client.get(self.url, {'name': 'Joao Augusto'})
        naver_2 = self.client.get(self.url, {'name': 'Fernanda Oliveira'})
        naver_3 = self.client.get(self.url, {'name': 'Deivison Pereira'})
        naver_4 = self.client.get(self.url, {'name': 'Priscila Marques'})
        self.assertEqual(len(naver_1.data), 1)
        self.assertEqual(len(naver_2.data), 1)
        self.assertEqual(len(naver_3.data), 1)
        self.assertEqual(len(naver_4.data), 1)
        self.assertEqual(
            json.dumps(naver_1.data[0]),
            json.dumps(self.expected_navers_list[0]))
        self.assertEqual(
            json.dumps(naver_2.data[0]),
            json.dumps(self.expected_navers_list[1]))
        self.assertEqual(
            json.dumps(naver_3.data[0]),
            json.dumps(self.expected_navers_list[2]))
        self.assertEqual(
            json.dumps(naver_4.data[0]),
            json.dumps(self.expected_navers_list[3]))
    
    @freeze_time('2020-08-24 22:55')
    def test_index_view_filter_by_company_time_in_years(self):
        response = self.client.get(self.url, {'company_time_in_years': '2'})
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]['id'], 1)
        self.assertEqual(response.data[1]['id'], 2)
        self.assertEqual(response.data[2]['id'], 3)
    
    @freeze_time('2020-08-24 22:55')
    def test_index_view_filter_by_company_time_in_months(self):
        response = self.client.get(self.url, {'company_time_in_months': '8'})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], 3)
    
    @freeze_time('2020-08-24 22:55')
    def test_index_view_filter_by_company_time_in_months_with_2_digits(self):
        response = self.client.get(self.url, {'company_time_in_months': '8,16'})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], 2)
    
    @freeze_time('2020-08-24 22:55')
    def test_index_view_filter_by_company_time_in_days(self):
        response = self.client.get(self.url, {'company_time_in_days': '500'})
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['id'], 2)
        self.assertEqual(response.data[1]['id'], 3)
    
    @freeze_time('2020-08-24 22:55')
    def test_index_view_filter_by_company_time_in_days_with_2_digits(self):
        response = self.client.get(self.url, {'company_time_in_days': '0,300'})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], 3)
    
    @freeze_time('2020-08-24 22:55')
    def test_index_view_filter_by_job_role_desenvoledor_react(self):
        response = self.client.get(self.url, {'job_role': 'Desenvolvedor React'})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], 1)
    
    @freeze_time('2020-08-24 22:55')
    def test_index_view_filter_by_job_role_desenvoledora_backend(self):
        response = self.client.get(self.url, {'job_role': 'Desenvolvedora Backend'})
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], 2)
