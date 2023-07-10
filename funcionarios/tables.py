# tables.py
import django_tables2 as tables
from funcionarios.models import Funcionario

class FuncionarioTable(tables.Table):
   class Meta:
       model = Funcionario