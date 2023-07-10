from django.urls import path
from . import views
from .views import PerfilListView

urlpatterns = [
   path('', PerfilListView.as_view()),
   path('cadastrar',views.perfil_cadastrar),
   path('editar/<id>',views.perfil_editar),
   path('remover/<id>',views.perfil_remover),
   path('<id>', views.perfil_detail , name="perfil_detail"),
]

