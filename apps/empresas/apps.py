# apps.py dentro do diretório 'empresas'
from django.apps import AppConfig

class EmpresasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.empresas'  # Certifique-se de que o nome está correto.
