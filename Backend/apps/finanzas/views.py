from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from .models import CategoriaGasto, Transaccion
from .serializers import CategoriaGastoSerializer, TransaccionSerializer


class CategoriaGastoViewSet(viewsets.ModelViewSet):
    """CRUD de categorías de gasto/ingreso."""
    queryset = CategoriaGasto.objects.all()
    serializer_class = CategoriaGastoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'tipo']


class TransaccionViewSet(viewsets.ModelViewSet):
    """
    CRUD de transacciones financieras.
    Filtros: ?finca=<uuid> &tipo=ingreso &categoria=<uuid>
             &fecha_desde=YYYY-MM-DD &fecha_hasta=YYYY-MM-DD
    Extra:   GET /api/v1/finanzas/transacciones/balance/ → resumen financiero por finca
    """
    queryset = Transaccion.objects.select_related('finca', 'categoria').all()
    serializer_class = TransaccionSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['fecha', 'monto']

    def get_queryset(self):
        qs = super().get_queryset()
        finca_id = self.request.query_params.get('finca')
        tipo = self.request.query_params.get('tipo')
        categoria_id = self.request.query_params.get('categoria')
        fecha_desde = self.request.query_params.get('fecha_desde')
        fecha_hasta = self.request.query_params.get('fecha_hasta')

        if finca_id:
            qs = qs.filter(finca_id=finca_id)
        if tipo:
            qs = qs.filter(tipo=tipo)
        if categoria_id:
            qs = qs.filter(categoria_id=categoria_id)
        if fecha_desde:
            qs = qs.filter(fecha__gte=fecha_desde)
        if fecha_hasta:
            qs = qs.filter(fecha__lte=fecha_hasta)
        return qs

    @action(detail=False, methods=['get'])
    def balance(self, request):
        """
        GET /api/v1/finanzas/transacciones/balance/?finca=<uuid>
        Retorna total ingresos, egresos y balance neto.
        """
        qs = self.get_queryset()
        resumen = qs.aggregate(
            total_ingresos=Sum('monto', filter=__import__('django.db.models', fromlist=['Q']).Q(tipo='ingreso')),
            total_egresos=Sum('monto', filter=__import__('django.db.models', fromlist=['Q']).Q(tipo='egreso')),
        )
        ingresos = resumen['total_ingresos'] or 0
        egresos = resumen['total_egresos'] or 0
        resumen['balance_neto'] = ingresos - egresos
        return Response(resumen)
