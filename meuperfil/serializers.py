from rest_framework import serializers
from .models import Perfil

class PerfilSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perfil
        fields = ['name','email','bloco','unidade','observacoes']