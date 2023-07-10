from django.db import models

class Funcionario(models.Model):
    GENERO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("O", "Outros")
    )
    TIPO_USUARIO_CHOICES = (
        ("C", "Condômino"),
        ("S", "Síndico"),
        ("O", "Outros")
    )
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,blank=True)
    cargo  = models.CharField(max_length=100)
    rg  = models.CharField(max_length=20)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES, blank=False, null=False,default="O")
    tipo_usuario = models.CharField(max_length=1, choices=TIPO_USUARIO_CHOICES, blank=False, null=False,default="O")
    observacoes = models.TextField(max_length=1000,blank=True)
    def __str__(self):
        return self.name



