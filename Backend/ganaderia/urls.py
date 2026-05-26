from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # API v1
    path('api/v1/fincas/',            include('apps.fincas.urls')),
    path('api/v1/usuarios/',          include('apps.usuarios.urls')),
    path('api/v1/animales/',          include('apps.animales.urls')),
    path('api/v1/producciones/',      include('apps.producciones.urls')),
    path('api/v1/eventos-sanitarios/',include('apps.eventos_sanitarios.urls')),
    path('api/v1/pesajes/',           include('apps.pesajes.urls')),
    path('api/v1/partos/',            include('apps.partos.urls')),
    path('api/v1/finanzas/',          include('apps.finanzas.urls')),
]
