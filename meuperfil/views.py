from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PerfilForm
from .models import Perfil
from django.contrib import messages
from django.views.generic import ListView

def perfil_cadastrar(request):

   if request.method == 'POST':
       form = PerfilForm(request.POST)
       if form.is_valid():
           form.save()
           messages.success(request, 'Cadastro de perfil efetuado com sucesso.')
           return redirect("/meuperfil")


   form = PerfilForm()
   return render(request, 'cadastrar.html',{'form':form})
def perfil_editar(request, id):
   instance = Perfil.objects.get(id = id)
   form = PerfilForm(request.POST or None,instance=instance)
   if form.is_valid():
       form.save()
       messages.success(request, 'Cadastro de perfil editado com sucesso.')
       return redirect("/meuperfil")
   return render(request, 'editar.html',{'form':form})

def perfil_remover(request, id):
   if request.method == 'POST':
       instance = Perfil.objects.get(id = id)
       instance.delete()
       messages.success(request, 'Cadastro de perfil removido com sucesso.')
       return redirect("/meuperfil")

   # dictionary for initial data with
   # field names as keys
   context ={}
   # add the dictionary during initialization
   context["data"] = Perfil.objects.get(id = id)
       
   return render(request, "remover.html", context)




def perfil_detail(request, id):

   # dictionary for initial data with
   # field names as keys
   context ={}
   # add the dictionary during initialization
   context["data"] = Perfil.objects.get(id = id)
       
   return render(request, "meuperfil.html", context)

class PerfilListView(ListView):
   model = Perfil
   template_name = 'listar.html'
