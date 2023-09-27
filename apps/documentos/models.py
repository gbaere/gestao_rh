from django.db import models

class Documento(models.Model):
    descricao = models.CharField(max_length=120)

    def __str__(self):
        return self.descricao

