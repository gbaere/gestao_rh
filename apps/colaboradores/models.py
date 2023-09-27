from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa

class Colaborador(models.Model):
    nome = models.CharField(max_length=150)
    data_nascimento = models.DateField(help_text="Data de nascimento")
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos_alocado = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(
        Empresa, on_delete=models.PROTECT, null=True, blank=True)
    imagem = models.ImageField()
    de_ferias = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('list_colaboradores')

    class Meta:
        ordering = ['nome']
        verbose_name_plural = 'Colaboradores'

    def __str__(self):
        return self.nome




