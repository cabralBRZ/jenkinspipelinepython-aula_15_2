from django.db import models

class Perfil(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,blank=True)
    bloco = models.CharField(max_length=2,default='SB')
    unidade = models.CharField(max_length=5,default='SU')
    observacoes = models.TextField(max_length=1000,blank=True)
    def __str__(self):
        return self.name



