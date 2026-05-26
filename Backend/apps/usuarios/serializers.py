import hashlib

from rest_framework import serializers
from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'email', 'rol', 'finca', 'created_at']
        read_only_fields = ['id', 'created_at']


class UsuarioCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'email', 'password', 'rol', 'finca']
        read_only_fields = ['id']
        extra_kwargs = {
            'rol': {'required': False},
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data['password_hash'] = hashlib.sha256(password.encode()).hexdigest()
        validated_data.setdefault('rol', 'propietario')
        return super().create(validated_data)
