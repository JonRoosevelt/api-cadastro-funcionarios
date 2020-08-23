import factory
from . import models
# from django.contrib.auth.models import User
from providers.providers import Professions

factory.Faker.add_provider(Professions)

DjangoModelFactory = factory.django.DjangoModelFactory


class UserFactory(DjangoModelFactory):
    email = factory.Faker('email')

    class Meta:
        model = models.User


class ProjetoFactory(DjangoModelFactory):
    name = factory.Faker('company')

    class Meta:
        model = models.Projeto


class NaverFactory(DjangoModelFactory):
    name = factory.LazyAttribute(lambda o: o.user.last_name)
    birthdate = factory.Faker('date_of_birth')
    admission_date = factory.Faker('date')
    job_role = factory.Faker('role')
    created_by = factory.SubFactory(UserFactory)

    class Meta:
        model = models.Naver


class NaverProjetoFactory(DjangoModelFactory):
    projeto = factory.SubFactory(ProjetoFactory)
    naver = factory.SubFactory(NaverFactory)
    
    class Meta:
        model = models.NaverProjeto