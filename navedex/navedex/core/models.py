from django.contrib.auth.models import User
from django.db import models
from .helpers import NaverBaseModel


class Projeto(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    class Meta:
        db_table = 'projeto'


class Naver(NaverBaseModel):
    user = models.OneToOneField(
        User, related_name='naver', on_delete=models.PROTECT)
    name = models.CharField(max_length=200, db_index=True)
    birthdate = models.DateField(
        db_column='data_nascimento',
        verbose_name='Data de Nascimento',
        null=False
    )
    admission_date = models.DateField(
        db_column='data_admissao',
        verbose_name='Data de admissão',
        null=False
    )
    job_role = models.CharField(max_length=100, db_index=True)
    projects = models.ManyToManyField(
        Projeto,
        through='NaverProjeto',
        related_name='navers',
        blank=True,
    )

    class Meta:
        db_table = 'naver'


class NaverProjeto(NaverBaseModel):
    projeto = models.ForeignKey(
        Projeto, models.PROTECT, verbose_name='projeto', db_column='projeto_id'
    )
    naver = models.ForeignKey(Naver, models.PROTECT,
                              verbose_name='naver', db_column='naver_id')

    class Meta:
        unique_together = ('projeto', 'naver')
        verbose_name = 'Projeto x Naver'
        verbose_name_plural = 'Projetos x Navers'
        db_table = 'naver_projeto'
