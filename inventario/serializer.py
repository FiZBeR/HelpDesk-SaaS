from rest_framework import serializers
from .models import EquipoModel

class EquipoSerializer (serializers.ModelSerializer):
    class Meta:
        model = EquipoModel
        fields = ['numero_serie', 'tipo', 'estado']