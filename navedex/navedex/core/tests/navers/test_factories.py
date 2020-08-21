from django.test.testcases import TestCase
from navedex.core.factories import UserFactory, NaverFactory, ProjetoFactory, NaverProjetoFactory
from navedex.core.models import User, Naver, Projeto, NaverProjeto
from django.utils.dateparse import parse_date


class FactoriesTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory(
            username='johndoe',
            first_name='John',
            last_name='Doe',
            email='johndoe@doe.com'
        )
        cls.naver = NaverFactory(
            user=cls.user,
            name='John Doe',
            birthdate=parse_date('1990-10-12'),
            admission_date=parse_date('2011-08-01'),
            job_role='Desenvolvedor'
        )
        cls.projeto = ProjetoFactory(
            name='Any project'
        )
        cls.naver_projeto = NaverProjetoFactory(
            projeto=cls.projeto,
            naver=cls.naver
        )

    def test_if_an_user_instance_was_created(self):
        user = User.objects.all()
        self.assertEqual(len(user), 1)
        self.assertEqual(user[0].username, 'johndoe')
        self.assertEqual(user[0].first_name, 'John')
        self.assertEqual(user[0].last_name, 'Doe')
        self.assertEqual(user[0].email, 'johndoe@doe.com')

    def test_if_an_naver_instance_was_created(self):
        naver = Naver.objects.all()
        self.assertEqual(len(naver), 1)
        self.assertEqual(naver[0].user, self.user)
        self.assertEqual(naver[0].name, 'John Doe')
        self.assertEqual(naver[0].birthdate, parse_date('1990-10-12'))
        self.assertEqual(naver[0].admission_date, parse_date('2011-08-01'))
        self.assertEqual(naver[0].job_role, 'Desenvolvedor')

    def test_if_projeto_instance_was_created(self):
        projeto = Projeto.objects.all()
        self.assertEqual(len(projeto), 1)
        self.assertEqual(projeto[0].name, 'Any project')

    def test_if_a_naver_projeto_instance_was_created(self):
        naver_projeto = NaverProjeto.objects.all()
        user = User.objects.all()
        naver = Naver.objects.all()
        projeto = Projeto.objects.all()
        self.assertEqual(len(naver_projeto), 1)
        self.assertEqual(len(user), 1)
        self.assertEqual(len(naver), 1)
        self.assertEqual(len(projeto), 1)
        self.assertEqual(naver_projeto[0].projeto.name, 'Any project')
        self.assertEqual(naver_projeto[0].naver.name, 'John Doe')
