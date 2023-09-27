from django.db import models
from apps.colaboradores.models import Colaborador


class RegistrarHoraExtra(models.Model):
    motivo = models.CharField(max_length=200)
    colaborador = models.ForeignKey(Colaborador, on_delete=models.PROTECT)

    class Meta:
        ordering = ['colaborador']
        verbose_name_plural = 'RegistrarHorasExtras'

    def __str__(self):
        return self.motivo



