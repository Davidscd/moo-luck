from rest_framework import viewsets, filters
from .models import Finca
from .serializers import FincaSerializer


class FincaViewSet(viewsets.ModelViewSet):
    queryset = Finca.objects.all()
    serializer_class = FincaSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'municipio', 'departamento']
    ordering_fields = ['nombre', 'created_at', 'hectareas']

    def get_queryset(self):
        qs = super().get_queryset()
        propietario_id = self.request.query_params.get('propietario')
        if propietario_id:
            qs = qs.filter(propietario_id=propietario_id)
        return qs
