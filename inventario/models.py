from django.db import models

TIPO_EQUIPO = [
    ('laptop', 'Laptop'),
    ('monitor', 'Monitor'),
    ('servidor', 'Servidor')
]

ESTADO_EQUIPO = [
    ('operativo', 'Operativo'),
    ('en_reparacion', 'En reparacion'),
    ('dado_de_baja', 'Dado de baja')
]

# Create your models here.
class EquipoModel (models.Model):
    numero_serie = models.CharField(max_length=20, unique=True)
    tipo = models.CharField(max_length=20, choices=TIPO_EQUIPO)
    estado = models.CharField(max_length=20, choices=ESTADO_EQUIPO, default='operativo')