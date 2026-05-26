from rest_framework import serializers
from .models import CategoriaGasto, Transaccion


class CategoriaGastoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaGasto
        fields = '__all__'
        read_only_fields = ['id']


class TransaccionSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)
    finca_nombre = serializers.CharField(source='finca.nombre', read_only=True)

    class Meta:
        model = Transaccion
        fields = '__all__'
        read_only_fields = ['id']
