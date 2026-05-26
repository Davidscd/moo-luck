from rest_framework import viewsets, filters
from .models import Finca
from .serializers import FincaSerializer


class FincaViewSet(viewsets.ModelViewSet):
    """
    CRUD completo para Fincas.
    GET    /api/v1/fincas/          → listar todas
    POST   /api/v1/fincas/          → crear nueva
    GET    /api/v1/fincas/{id}/     → obtener una
    PUT    /api/v1/fincas/{id}/     → actualizar completa
    PATCH  /api/v1/fincas/{id}/     → actualizar parcial
    DELETE /api/v1/fincas/{id}/     → eliminar
    """
    queryset = Finca.objects.all()
    serializer_class = FincaSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'municipio', 'departamento']
    ordering_fields = ['nombre', 'created_at', 'hectareas']
