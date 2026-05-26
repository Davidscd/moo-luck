from rest_framework import serializers
from .models import Produccion


class ProduccionSerializer(serializers.ModelSerializer):
    animal_codigo = serializers.CharField(source='animal.codigo', read_only=True)

    class Meta:
        model = Produccion
        fields = '__all__'
        read_only_fields = ['id', 'litros_total']
