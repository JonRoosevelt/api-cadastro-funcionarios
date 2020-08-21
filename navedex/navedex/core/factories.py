import factory
from . import models
# from django.contrib.auth.models import User
from ..providers.providers import Professions

factory.Faker.add_provider(Professions)

DjangoModelFactory = factory.django.DjangoModelFactory


class UserFactory(DjangoModelFactory):
    username = factory.Faker('user_name')
    first_name = factory.Faker('name')
    last_name = factory.Faker('name')
    email = factory.Faker('email')

    class Meta:
        model = models.User


class ProjetoFactory(DjangoModelFactory):
    name = factory.Faker('company')

    class Meta:
        model = models.Projeto


class NaverFactory(DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    name = factory.LazyAttribute(lambda o: o.user.last_name)
    birthdate = factory.Faker('date_of_birth')
    admission_date = factory.Faker('date')
    job_role = factory.Faker('role')

    class Meta:
        model = models.Naver


class NaverProjetoFactory(DjangoModelFactory):
    projeto = factory.SubFactory(ProjetoFactory)
    naver = factory.SubFactory(NaverFactory)
    
    class Meta:
        model = models.NaverProjeto