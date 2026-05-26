from rest_framework import viewsets, filters
from .models import Pesaje
from .serializers import PesajeSerializer


class PesajeViewSet(viewsets.ModelViewSet):
    """
    CRUD de pesajes.
    Filtros: ?animal=<uuid> &fecha_desde=YYYY-MM-DD &fecha_hasta=YYYY-MM-DD
    """
    queryset = Pesaje.objects.select_related('animal').all()
    serializer_class = PesajeSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['fecha', 'peso_kg']

    def get_queryset(self):
        qs = super().get_queryset()
        animal_id = self.request.query_params.get('animal')
        fecha_desde = self.request.query_params.get('fecha_desde')
        fecha_hasta = self.request.query_params.get('fecha_hasta')

        if animal_id:
            qs = qs.filter(animal_id=animal_id)
        if fecha_desde:
            qs = qs.filter(fecha__gte=fecha_desde)
        if fecha_hasta:
            qs = qs.filter(fecha__lte=fecha_hasta)
        return qs
