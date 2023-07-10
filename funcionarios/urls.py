from django.urls import path

from funcionarios import views
from funcionarios.views import FuncionarioListView

urlpatterns = [
   path('', FuncionarioListView.as_view()),
   path('cadastrar',views.funcionario_cadastrar),
   path('editar/<id>',views.funcionario_editar),
   path('remover/<id>',views.funcionario_remover),
   path('<id>', views.funcionario_detail , name="funcionario_detail"),
]

