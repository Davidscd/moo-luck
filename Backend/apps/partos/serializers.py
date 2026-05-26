from rest_framework import serializers
from .models import Parto


class PartoSerializer(serializers.ModelSerializer):
    madre_codigo = serializers.CharField(source='madre.codigo', read_only=True)

    class Meta:
        model = Parto
        fields = '__all__'
        read_only_fields = ['id']
