import hashlib

from django.utils import timezone
from rest_framework import authentication, exceptions
from .models import AuthToken


class UsuarioTokenAuthentication(authentication.BaseAuthentication):
    keyword = 'Bearer'

    def authenticate(self, request):
        header = authentication.get_authorization_header(request).decode('utf-8')
        if not header:
            return None

        parts = header.split()
        if len(parts) != 2 or parts[0] != self.keyword:
            raise exceptions.AuthenticationFailed('Token invalido.')

        token_hash = hashlib.sha256(parts[1].encode()).hexdigest()
        token = AuthToken.objects.select_related('usuario').filter(key_hash=token_hash).first()
        if not token:
            raise exceptions.AuthenticationFailed('Token invalido o expirado.')

        token.last_used_at = timezone.now()
        token.save(update_fields=['last_used_at'])
        return (token.usuario, token)
