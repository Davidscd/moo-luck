import hashlib
import secrets

from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import AuthToken, Usuario
from .serializers import UsuarioSerializer, UsuarioCreateSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.select_related('finca').all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nombre', 'email', 'rol']
    ordering_fields = ['nombre', 'created_at', 'rol']

    def get_permissions(self):
        if self.action in ['create', 'login']:
            return [AllowAny()]
        return super().get_permissions()

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if getattr(user, 'rol', None) == 'admin':
            return qs
        if getattr(user, 'id', None):
            return qs.filter(id=user.id)
        return qs.none()

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

        return Response(self._session_payload(user))

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = Usuario.objects.get(id=response.data['id'])
        return Response(self._session_payload(user), status=response.status_code)

    @action(detail=False, methods=['post'])
    def logout(self, request):
        if request.auth:
            request.auth.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def _session_payload(self, user):
        raw_token = secrets.token_urlsafe(40)
        token_hash = hashlib.sha256(raw_token.encode()).hexdigest()
        AuthToken.objects.create(usuario=user, key_hash=token_hash)
        payload = UsuarioSerializer(user).data
        payload['token'] = raw_token
        return payload
