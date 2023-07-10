from django import forms
from funcionarios.models import Funcionario

class FuncionarioForm(forms.ModelForm):
    db_table = 'Funcionario'
    class Meta:
        model = Funcionario
        fields = ('nome', 'genero', 'email', 'cargo', 'rg' ,'observacoes')