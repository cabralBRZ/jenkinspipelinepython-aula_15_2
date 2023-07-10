from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
   path('meuperfil/', include('meuperfil.urls')),
   path('funcionarios/', include('funcionarios.urls')),
   path('perfil/', include('meuperfil.urls_api')),
   path('admin/', admin.site.urls),
   path('users/', include('users.urls')),
   path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
   path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
