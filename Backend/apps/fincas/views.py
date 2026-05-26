from rest_framework import viewsets, filters
from .models import Finca
from .serializers import FincaSerializer
from apps.usuarios.permissions import is_admin


class FincaViewSet(viewsets.ModelViewSet):
    queryset = Finca.objects.all()
    serializer_class = FincaSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'municipio', 'departamento']
    ordering_fields = ['nombre', 'created_at', 'hectareas']

    def get_queryset(self):
        qs = super().get_queryset()
        if not is_admin(self.request.user):
            qs = qs.filter(propietario_id=self.request.user.id)
        propietario_id = self.request.query_params.get('propietario')
        if propietario_id:
            qs = qs.filter(propietario_id=propietario_id)
        return qs

    def perform_create(self, serializer):
        propietario_id = self.request.user.id
        if is_admin(self.request.user):
            propietario_id = self.request.data.get('propietario_id') or propietario_id
        serializer.save(propietario_id=propietario_id)
