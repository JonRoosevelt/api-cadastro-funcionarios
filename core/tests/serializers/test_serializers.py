from django.test.testcases import TestCase
from core.factories import UserFactory, NaverFactory, ProjetoFactory, NaverProjetoFactory
from core.models import User, Naver, Projeto, NaverProjeto
from core.serializers import UserSerializer, NaverSerializer, ProjetoSerializer, NaverProjetoSerializer
from django.utils.dateparse import parse_date


class SerializersTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory(
            email='johndoe@doe.com'
        )
        cls.naver = NaverFactory(
            name='John Doe',
            birthdate=parse_date('1990-10-12'),
            admission_date=parse_date('2011-08-01'),
            job_role='Desenvolvedor',
            created_by=cls.user,
        )
        cls.projeto = ProjetoFactory(
            name='Any project'
        )
        cls.projeto_naver = NaverProjetoFactory(
            projeto=cls.projeto,
            naver=cls.naver
        )

    def test_if_user_serializers_returns_as_expected(self):
        user = User.objects.first()
        serializer = UserSerializer(user)
        self.assertEqual(serializer.data['email'], 'johndoe@doe.com')

    def test_if_naver_serializer_returns_as_expected(self):
        naver = Naver.objects.first()
        serializer = NaverSerializer(naver)
        self.assertEqual(serializer.data['id'], 1)
        self.assertEqual(serializer.data['name'], 'John Doe')
        self.assertEqual(serializer.data['birthdate'], '1990-10-12')
        self.assertEqual(serializer.data['admission_date'], '2011-08-01')
        self.assertEqual(serializer.data['job_role'], 'Desenvolvedor')

    def test_if_projeto_serializer_returns_as_expected(self):
        projeto = Projeto.objects.first()
        serializer = ProjetoSerializer(projeto)
        self.assertEqual(serializer.data['id'], 1)
        self.assertEqual(serializer.data['name'], 'Any project')

    def test_if_projeto_naver_serializer_returns_one_to_one_as_expected(self):
        projeto_naver = NaverProjeto.objects.first()
        serializer = NaverProjetoSerializer(projeto_naver)
        self.assertEqual(serializer.data['projeto'], 'Any project')
        self.assertEqual(serializer.data['naver'], 'John Doe')
