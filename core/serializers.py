from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = models.User(**validated_data)
        user.set_password(password)
        user.save()
        return user


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


class NaverDetailsSerializer(serializers.ModelSerializer):
    projects = ProjetoSerializer(many=True)

    class Meta:
        model = models.Naver
        fields = [
            'id',
            'name',
            'birthdate',
            'admission_date',
            'job_role',
            'projects',
        ]
