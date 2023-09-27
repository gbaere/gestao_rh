from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=200, help_text="Nome da empresa")

    class Meta:
        ordering = ['nome']
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nome




