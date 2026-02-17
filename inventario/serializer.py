from rest_framework import serializers
from .models import EquipoModel

class EquipoSerializer (serializers.ModelSerializer):
    class Meta:
        model = EquipoModel
        field = ['numero_serie', 'equipo', 'estado']