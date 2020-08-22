from . import models
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('__all__')


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


class NaverProjetoSerializer(serializers.ModelSerializer):
    projeto = serializers.CharField(source='projeto.name')
    naver = serializers.CharField(source='naver.name')

    class Meta:
        model = models.NaverProjeto
        fields = [
            'projeto',
            'naver',
        ]
