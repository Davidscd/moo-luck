from rest_framework import serializers
from .models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    madre_codigo = serializers.CharField(source='madre.codigo', read_only=True)
    padre_codigo = serializers.CharField(source='padre.codigo', read_only=True)
    finca_nombre = serializers.CharField(source='finca.nombre', read_only=True)

    class Meta:
        model = Animal
        fields = '__all__'
        read_only_fields = ['id', 'created_at']


class AnimalListSerializer(serializers.ModelSerializer):
    """Versión ligera para listados."""
    class Meta:
        model = Animal
        fields = ['id', 'codigo', 'nombre', 'raza', 'sexo', 'estado', 'proposito', 'finca']
