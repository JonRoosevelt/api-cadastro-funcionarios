from .decorators import with_author
from django.db import models


class BaseModel(models.Model):
    def __str__(self):
        if hasattr(self, 'nome') and self.nome:
            return self.nome
        if hasattr(self, 'name') and self.name:
            return self.name
        return super().__str__()

    class Meta:
        abstract = True


@with_author
class NaverBaseModel(BaseModel):
    created_at = models.DateTimeField(auto_now_add=True, db_column='criado_em')
    updated_at = models.DateTimeField(auto_now=True, db_column='atualizado_em')

    class Meta:
        abstract = True
