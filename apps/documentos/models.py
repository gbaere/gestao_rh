from django.db import models
from apps.colaboradores.models import Colaborador

class Documento(models.Model):
    descricao = models.CharField(max_length=120)
    proprietario = models.ForeignKey(Colaborador, on_delete=models.PROTECT)

    class Meta:
        ordering = ['descricao']
        verbose_name_plural = 'Documentos'

    def __str__(self):
        return self.descricao

