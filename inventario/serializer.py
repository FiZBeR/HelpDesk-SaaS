from rest_framework import serializers
from .models import EquipoModel

class EquipoSerializer (serializers.ModelSerializer):
    class Meta:
        model = EquipoModel
        fields = ['id', 'numero_serie', 'tipo', 'estado']