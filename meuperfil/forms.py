from django import forms
from .models import Perfil

class PerfilForm(forms.ModelForm):
    db_table = 'perfil'
    class Meta:
        model = Perfil
        fields = ('name','email','bloco','unidade','observacoes')