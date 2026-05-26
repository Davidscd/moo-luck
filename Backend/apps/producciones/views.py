from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from .models import Produccion
from .serializers import ProduccionSerializer


class ProduccionViewSet(viewsets.ModelViewSet):
    """
    CRUD de producciones de leche.
    Filtros: ?animal=<uuid> &fecha=YYYY-MM-DD &fecha_desde=YYYY-MM-DD &fecha_hasta=YYYY-MM-DD
    Extra: GET /api/v1/producciones/resumen/?animal=<uuid> → total por animal
    """
    queryset = Produccion.objects.select_related('animal', 'registrado_por').all()
    serializer_class = ProduccionSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['fecha', 'litros_total']

    def get_queryset(self):
        qs = super().get_queryset()
        animal_id = self.request.query_params.get('animal')
        fecha = self.request.query_params.get('fecha')
        fecha_desde = self.request.query_params.get('fecha_desde')
        fecha_hasta = self.request.query_params.get('fecha_hasta')

        if animal_id:
            qs = qs.filter(animal_id=animal_id)
        if fecha:
            qs = qs.filter(fecha=fecha)
        if fecha_desde:
            qs = qs.filter(fecha__gte=fecha_desde)
        if fecha_hasta:
            qs = qs.filter(fecha__lte=fecha_hasta)
        return qs

    @action(detail=False, methods=['get'])
    def resumen(self, request):
        """GET /api/v1/producciones/resumen/ → total de litros agrupado por animal"""
        animal_id = request.query_params.get('animal')
        qs = self.get_queryset()
        if animal_id:
            qs = qs.filter(animal_id=animal_id)

        total = qs.aggregate(
            total_manana=Sum('litros_manana'),
            total_tarde=Sum('litros_tarde'),
            total_general=Sum('litros_total'),
        )
        return Response(total)
