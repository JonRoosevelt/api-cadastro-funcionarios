from django.test import TestCase
from core.factories import NaverFactory
from core.filters import NaversIndexFilter
from core.models import Naver
from django.utils.dateparse import parse_date


class FilterNaverByYearTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.navers_dict = dict(
            naver_1=NaverFactory(
                name="Joao Augusto",
                birthdate=parse_date('1990-10-12'),
                admission_date=parse_date('2018-01-02'),
                job_role='Desenvolvedor React',
            ),
            naver_2=NaverFactory(
                name='Fernanda Oliveira',
                birthdate=parse_date('1995-08-06'),
                admission_date=parse_date('2019-05-03'),
                job_role='Desenvolvedora Backend',
            ),
            naver_3=NaverFactory(
                name='Deivison Pereira',
                birthdate=parse_date('1999-02-03'),
                admission_date=parse_date('2020-01-04'),
                job_role='Estagiário Teste',
            ),
            naver_4=NaverFactory(
                name='Priscila Marques',
                birthdate=parse_date('1987-01-23'),
                admission_date=parse_date('2014-02-02'),
                job_role='Gerente de Projetos',
            )
        )

        cls.queryset = Naver.objects.all()
        cls.filterset = NaversIndexFilter

    def test_filter_navers_by_company_time_last_two_years(self):
        filtered_queryset = self.filterset().filter_company_time(
            self.queryset, 'years', '0,2')
        self.assertEqual(len(filtered_queryset), 3)
        self.assertEqual(filtered_queryset[0].id, 1)
        self.assertEqual(filtered_queryset[1].id, 2)
        self.assertEqual(filtered_queryset[2].id, 3)

    def test_filters_navers_by_company_times_greater_than_three_years(self):
        filtered_queryset = self.filterset().filter_company_time(
            self.queryset, 'years', '3,10')
        self.assertEqual(len(filtered_queryset), 1)
        self.assertEqual(filtered_queryset[0].id, 4)

    def test_filters_navers_by_company_times_for_the_last_1_year(self):
        filtered_queryset = self.filterset().filter_company_time(self.queryset, 'years', '0')
        self.assertEqual(len(filtered_queryset), 1)


class FilterNaverByMonthTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.navers_dict = dict(
            naver_1=NaverFactory(
                name="Joao Augusto",
                birthdate=parse_date('1990-10-12'),
                admission_date=parse_date('2018-01-02'),
                job_role='Desenvolvedor React',
            ),
            naver_2=NaverFactory(
                name='Fernanda Oliveira',
                birthdate=parse_date('1995-08-06'),
                admission_date=parse_date('2019-05-03'),
                job_role='Desenvolvedora Backend',
            ),
            naver_3=NaverFactory(
                name='Deivison Pereira',
                birthdate=parse_date('1999-02-03'),
                admission_date=parse_date('2020-01-04'),
                job_role='Estagiário Teste',
            ),
            naver_4=NaverFactory(
                name='Priscila Marques',
                birthdate=parse_date('1987-01-23'),
                admission_date=parse_date('2014-02-02'),
                job_role='Gerente de Projetos',
            )
        )

        cls.queryset = Naver.objects.all()
        cls.filterset = NaversIndexFilter

    def test_filter_navers_by_company_time_last_two_months(self):
        filtered_queryset = self.filterset().filter_company_time(
            self.queryset, 'months', '2')
        self.assertEqual(len(filtered_queryset), 0)

    def test_filter_navers_by_company_time_last_ten_months(self):
        filtered_queryset = self.filterset().filter_company_time(
            self.queryset, 'months', '0,10')
        self.assertEqual(len(filtered_queryset), 1)

    def test_filter_navers_by_company_time_last_sixteen_months(self):
        filtered_queryset = self.filterset().filter_company_time(
            self.queryset, 'months', '0,16')
        self.assertEqual(len(filtered_queryset), 2)

    def test_filters_navers_by_company_times_between_eight_months_and_sixteen_months(self):
        filtered_queryset = self.filterset().filter_company_time(
            self.queryset, 'months', '8,16')
        self.assertEqual(len(filtered_queryset), 1)
        self.assertEqual(filtered_queryset[0].id, 2)

    def test_filters_navers_by_company_times_for_the_last_eight_month(self):
        filtered_queryset = self.filterset().filter_company_time(
            self.queryset, 'months', '8')
        self.assertEqual(len(filtered_queryset), 1)


class FilterNaverByDaysTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.navers_dict = dict(
            naver_1=NaverFactory(
                name="Joao Augusto",
                birthdate=parse_date('1990-10-12'),
                admission_date=parse_date('2018-01-02'),
                job_role='Desenvolvedor React',
            ),
            naver_2=NaverFactory(
                name='Fernanda Oliveira',
                birthdate=parse_date('1995-08-06'),
                admission_date=parse_date('2019-05-03'),
                job_role='Desenvolvedora Backend',
            ),
            naver_3=NaverFactory(
                name='Deivison Pereira',
                birthdate=parse_date('1999-02-03'),
                admission_date=parse_date('2020-01-04'),
                job_role='Estagiário Teste',
            ),
            naver_4=NaverFactory(
                name='Priscila Marques',
                birthdate=parse_date('1987-01-23'),
                admission_date=parse_date('2014-02-02'),
                job_role='Gerente de Projetos',
            )
        )

        cls.queryset = Naver.objects.all()
        cls.filterset = NaversIndexFilter

    def test_filter_navers_by_company_time_last_500_days(self):
        filtered_queryset = self.filterset().filter_company_time(
            self.queryset, 'days', '500')
        self.assertEqual(len(filtered_queryset), 2)

    def test_filter_navers_by_company_time_last_300_days(self):
        filtered_queryset = self.filterset().filter_company_time(
            self.queryset, 'days', '0,300')
        self.assertEqual(len(filtered_queryset), 1)
