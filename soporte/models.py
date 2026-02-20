from django.db import models
from inventario.models import EquipoModel
from django.conf import settings
import uuid
from django.utils import timezone


PRIORIDAD_TICKET = [
    ('baja', 'Baja'),
    ('media', 'Media'),
    ('alta', 'Alta'),
    ('critica', 'Critica')
]

ESTADO_TICKET = [
    ('abierto', 'Abierto'),
    ('en_progreso', 'En Progreso'),
    ('resuelto', 'Resuelto')
]
# Create your models here.


class TicketModel (models.Model):
    codigo = models.CharField(max_length=15, unique=True, editable=False)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    prioridad = models.CharField(max_length=20, choices=PRIORIDAD_TICKET)
    estado = models.CharField(
        max_length=20, choices=ESTADO_TICKET, default='abierto')
    equipo = models.ForeignKey(
        EquipoModel, on_delete=models.CASCADE, related_name='tickets')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_cierre = models.DateTimeField(null=True, blank=True)
    cliente = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='tickets_creados')
    tecnico_asignado = models.ForeignKey(settings.AUTH_USER_MODEL,
                                         on_delete=models.SET_NULL,
                                         null=True,
                                         blank=True,
                                         related_name='tickets_asignados')

    def save(self, *args, **kwargs):
        if not self.pk:
            year = timezone.now().year
            corto = str(uuid.uuid4())[:4].upper()
            self.codigo = f"TK-{year}-{corto}"
            
        super().save(*args, **kwargs)


class ComentarioModel (models.Model):
    ticket = models.ForeignKey(
        TicketModel, on_delete=models.PROTECT, related_name='comentarios')
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='mis_comentarios'
    )
    texto = models.TextField()
    es_interno = models.BooleanField(default=False)
    fecha = models.DateTimeField(auto_now_add=True)
