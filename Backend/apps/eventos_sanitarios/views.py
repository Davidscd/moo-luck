from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import EventoSanitario
from .serializers import EventoSanitarioSerializer


class EventoSanitarioViewSet(viewsets.ModelViewSet):
    """
    CRUD de eventos sanitarios (vacunas, tratamientos, etc).
    Filtros: ?animal=<uuid> &tipo=vacuna &veterinario=<uuid>
    Extra:   GET /api/v1/eventos-sanitarios/proximos/ → eventos con proxima_fecha próxima
    """
    queryset = EventoSanitario.objects.select_related('animal', 'veterinario').all()
    serializer_class = EventoSanitarioSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['tipo', 'medicamento', 'descripcion']
    ordering_fields = ['fecha', 'proxima_fecha']

    def get_queryset(self):
        qs = super().get_queryset()
        animal_id = self.request.query_params.get('animal')
        tipo = self.request.query_params.get('tipo')
        veterinario_id = self.request.query_params.get('veterinario')

        if animal_id:
            qs = qs.filter(animal_id=animal_id)
        if tipo:
            qs = qs.filter(tipo__icontains=tipo)
        if veterinario_id:
            qs = qs.filter(veterinario_id=veterinario_id)
        return qs

    @action(detail=False, methods=['get'])
    def proximos(self, request):
        """GET /api/v1/eventos-sanitarios/proximos/ → eventos pendientes en los próximos 30 días"""
        from datetime import timedelta
        hoy = timezone.now().date()
        en_30_dias = hoy + timedelta(days=30)
        proximos = self.get_queryset().filter(
            proxima_fecha__gte=hoy,
            proxima_fecha__lte=en_30_dias
        ).order_by('proxima_fecha')
        serializer = self.get_serializer(proximos, many=True)
        return Response(serializer.data)
