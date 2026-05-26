from rest_framework import serializers
from .models import EventoSanitario


class EventoSanitarioSerializer(serializers.ModelSerializer):
    animal_codigo = serializers.CharField(source='animal.codigo', read_only=True)
    veterinario_nombre = serializers.CharField(source='veterinario.nombre', read_only=True)

    class Meta:
        model = EventoSanitario
        fields = '__all__'
        read_only_fields = ['id']
