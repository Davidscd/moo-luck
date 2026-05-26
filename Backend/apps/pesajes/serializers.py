from rest_framework import serializers
from .models import Pesaje


class PesajeSerializer(serializers.ModelSerializer):
    animal_codigo = serializers.CharField(source='animal.codigo', read_only=True)

    class Meta:
        model = Pesaje
        fields = '__all__'
        read_only_fields = ['id']
