import hashlib

from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Usuario
from .serializers import UsuarioSerializer, UsuarioCreateSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.select_related('finca').all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'email', 'rol']
    ordering_fields = ['nombre', 'created_at', 'rol']

    def get_serializer_class(self):
        if self.action == 'create':
            return UsuarioCreateSerializer
        return UsuarioSerializer

    @action(detail=False, methods=['post'])
    def login(self, request):
        email = request.data.get('email', '').strip().lower()
        password = request.data.get('password', '')

        if not email or not password:
            return Response(
                {'detail': 'Email y password son requeridos.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        password_hash = hashlib.sha256(password.encode()).hexdigest()
        user = Usuario.objects.filter(email__iexact=email, password_hash=password_hash).first()

        if not user:
            return Response(
                {'detail': 'Credenciales invalidas.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(UsuarioSerializer(user).data)
