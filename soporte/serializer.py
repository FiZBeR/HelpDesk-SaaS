from rest_framework import serializers
from .models import TicketModel, ComentarioModel
from django.utils import timezone

class TicketSerializer(serializers.ModelSerializer):
    dias_abiertos = serializers.SerializerMethodField()

    class Meta: 
        model = TicketModel
        fields = ['titulo', 'descripcion', 'prioridad', 'estado', 'equipo', 'dias_abiertos']
        read_only_fields = ['codigo', 'fecha_cierre', 'cliente']
    
    def validate_equipo(self, value):
        
        if value.estado == 'dado_de_baja':
            raise serializers.ValidationError(
                {'error' : 'El equipo seleccionado esta dado de baja, no se puede crear el ticket'}
            )

        return value

    def validate(self, data):
        prioridad = data.get('prioridad')
        descripcion = data.get('descripcion')

        if prioridad != 'critica':
            return data

        if len(descripcion) < 50:
            raise serializers.ValidationError(
                {'error' : 'El ticket fue clasificado con un prioridad de nivel critico, la descripcion debe contener al menos 50 caracteres'}
            )
        
        return data

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['equipo'] = {
            'numero_serie' : instance.equipo.numero_serie,
            'estado' : instance.equipo.estado
        }

        return representation

    def get_dias_abiertos(self, instance):
        fecha_creacion = instance.fecha_creacion

        if instance.estado == 'resuelto' and instance.fecha_cierre:
            fecha_fin = instance.fecha_cierre
        else :
            fecha_fin = timezone.now()
        
        diferencia = fecha_fin - fecha_creacion

        return diferencia.days

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComentarioModel
        fields = ['ticket', 'texto']

    def validate_ticket (self, value):
        
        if value.estado == 'resuelto':
            raise serializers.ValidationError(
                'el Ticket ya fue resuelto, no se pueden agregar mas comentarios.'
            )
        
        return value