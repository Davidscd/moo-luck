from rest_framework import viewsets, filters
from .models import Parto
from .serializers import PartoSerializer


class PartoViewSet(viewsets.ModelViewSet):
    """
    CRUD de partos.
    Filtros: ?madre=<uuid> &tipo_parto=normal &estado_cria=vivo
    """
    queryset = Parto.objects.select_related('madre').all()
    serializer_class = PartoSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['fecha_parto']

    def get_queryset(self):
        qs = super().get_queryset()
        madre_id = self.request.query_params.get('madre')
        tipo_parto = self.request.query_params.get('tipo_parto')
        estado_cria = self.request.query_params.get('estado_cria')

        if madre_id:
            qs = qs.filter(madre_id=madre_id)
        if tipo_parto:
            qs = qs.filter(tipo_parto=tipo_parto)
        if estado_cria:
            qs = qs.filter(estado_cria=estado_cria)
        return qs
