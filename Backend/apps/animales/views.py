from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Animal
from .serializers import AnimalSerializer, AnimalListSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    """
    CRUD completo para Animales.
    Filtros disponibles: ?finca=<uuid> &estado=activo &sexo=hembra &proposito=leche
    Búsqueda: ?search=codigo_o_nombre
    """
    queryset = Animal.objects.select_related('madre', 'padre', 'finca').all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['codigo', 'nombre', 'raza']
    ordering_fields = ['codigo', 'fecha_nacimiento', 'created_at']

    def get_serializer_class(self):
        if self.action == 'list':
            return AnimalListSerializer
        return AnimalSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        # Filtros opcionales por query params
        finca_id = self.request.query_params.get('finca')
        estado = self.request.query_params.get('estado')
        sexo = self.request.query_params.get('sexo')
        proposito = self.request.query_params.get('proposito')

        if finca_id:
            qs = qs.filter(finca_id=finca_id)
        if estado:
            qs = qs.filter(estado=estado)
        if sexo:
            qs = qs.filter(sexo=sexo)
        if proposito:
            qs = qs.filter(proposito=proposito)
        return qs
