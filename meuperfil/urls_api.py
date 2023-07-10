from django.urls import path, include
from .models import Perfil
from rest_framework import routers, viewsets
from .serializers import PerfilSerializer

class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
router = routers.DefaultRouter()
router.register('', PerfilViewSet)

urlpatterns = [
   path('', include(router.urls)),
]