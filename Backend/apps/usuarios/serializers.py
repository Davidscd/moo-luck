from rest_framework import serializers
from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'email', 'rol', 'finca', 'created_at']
        read_only_fields = ['id', 'created_at']


class UsuarioCreateSerializer(serializers.ModelSerializer):
    """Serializer para crear usuarios, incluye password en texto plano."""
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'email', 'password', 'rol', 'finca']
        read_only_fields = ['id']

    def create(self, validated_data):
        import hashlib
        password = validated_data.pop('password')
        # Hash simple con SHA-256 (en producción usar bcrypt o argon2)
        validated_data['password_hash'] = hashlib.sha256(password.encode()).hexdigest()
        return super().create(validated_data)
