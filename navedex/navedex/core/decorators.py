from django.conf import settings
from django.db import models


def with_author(cls):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='+',
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        db_column='criado_por',
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='+',
        null=True,
        blank=True,
        on_delete=models.PROTECT,
        db_column='atualizado_por',
    )

    if not hasattr(cls, 'created_by'):
        cls.add_to_class('created_by', created_by)
    if not hasattr(cls, 'updated_by'):
        cls.add_to_class('updated_by', updated_by)

    return cls