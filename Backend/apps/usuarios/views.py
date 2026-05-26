from rest_framework import viewsets, filters
from .models import Usuario
from .serializers import UsuarioSerializer, UsuarioCreateSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    """
    CRUD completo para Usuarios.
    GET    /api/v1/usuarios/        → listar (sin password_hash)
    POST   /api/v1/usuarios/        → crear (recibe 'password' en texto plano)
    GET    /api/v1/usuarios/{id}/   → obtener uno
    PUT    /api/v1/usuarios/{id}/   → actualizar
    DELETE /api/v1/usuarios/{id}/   → eliminar
    """
    queryset = Usuario.objects.select_related('finca').all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'email', 'rol']
    ordering_fields = ['nombre', 'created_at', 'rol']

    def get_serializer_class(self):
        if self.action == 'create':
            return UsuarioCreateSerializer
        return UsuarioSerializer
