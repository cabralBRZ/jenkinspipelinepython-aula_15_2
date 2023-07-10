# tables.py
import django_tables2 as tables
from .models import Perfil

class PerfilTable(tables.Table):
   class Meta:
       model = Perfil