from django.shortcuts import render, redirect
from funcionarios.forms import FuncionarioForm
from funcionarios.models import Funcionario
from django.contrib import messages
from django.views.generic import ListView

def funcionario_cadastrar(request):

   if request.method == 'POST':
       form = FuncionarioForm(request.POST)
       if form.is_valid():
           form.save()
           messages.success(request, 'Cadastro de funcionario efetuado com sucesso.')
           return redirect("/funcionarios")


   form = FuncionarioForm()
   return render(request, 'cadastrar.html',{'form':form})
def funcionario_editar(request, id):
   instance = Funcionario.objects.get(id = id)
   form = FuncionarioForm(request.POST or None,instance=instance)
   if form.is_valid():
       form.save()
       messages.success(request, 'Cadastro de funcionario editado com sucesso.')
       return redirect("/funcionarios")
   return render(request, 'editar.html',{'form':form})

def funcionario_remover(request, id):
   if request.method == 'POST':
       instance = Funcionario.objects.get(id = id)
       instance.delete()
       messages.success(request, 'Cadastro de funcionario removido com sucesso.')
       return redirect("/funcionarios")

   # dictionary for initial data with
   # field names as keys
   context ={}
   # add the dictionary during initialization
   context["data"] = Funcionario.objects.get(id = id)
       
   return render(request, "funcionarios/remover.html", context)




def funcionario_detail(request, id):

   # dictionary for initial data with
   # field names as keys
   context ={}
   # add the dictionary during initialization
   context["data"] = Funcionario.objects.get(id = id)
       
   return render(request, "funcionario.html", context)

class FuncionarioListView(ListView):
   model = Funcionario
   template_name = 'listar.html'
