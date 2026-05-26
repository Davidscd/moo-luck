from rest_framework import serializers
from .models import Finca


class FincaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finca
        fields = '__all__'
        read_only_fields = ['id', 'created_at']
