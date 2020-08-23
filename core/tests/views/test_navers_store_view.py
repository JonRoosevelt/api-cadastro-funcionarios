import json

from django.test import TestCase
from django.utils.dateparse import parse_date
from rest_framework.test import APIClient

from core.models import Naver
from core.factories import UserFactory


class NaversStoreViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory(
            email='gerente@navedex.nv',
        )
        cls.naver = dict(
            name='Joao Augusto',
            birthdate='1990-10-12',
            admission_date='2018-01-02',
            job_role='Desenvolvedor React',
            created_by=cls.user.id,
        )

    def setUp(self):
        self.user = UserFactory()
        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.url = '/api/navers/'

    def test_store_view_creates_new_naver(self):
        response = self.client.post(self.url, data=self.naver)
        navers = Naver.objects.all()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(navers), 1)
        self.assertEqual(
            json.dumps(response.data['name']), 
            json.dumps(self.naver['name'])
        )
        self.assertEqual(
            json.dumps(response.data['birthdate']), 
            json.dumps(self.naver['birthdate'])
        )
        self.assertEqual(
            json.dumps(response.data['admission_date']), 
            json.dumps(self.naver['admission_date'])
        )
        self.assertEqual(
            json.dumps(response.data['job_role']), 
            json.dumps(self.naver['job_role'])
        )
