from . import models
from rest_framework import serializers


class NaverSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Naver
        fields = [
            'id',
            'name',
            'birthdate',
            'admission_date',
            'job_role',
        ]


class ProjetoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Projeto
        fields = [
            'id',
            'name'
        ]
