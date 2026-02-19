from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class UsuarioModel(AbstractUser):
    ROLES = [
        ('administrador', 'Administrador'),
        ('tecnico', 'Tecnico'),
        ('cliente', 'Cliente')
    ]

    rol = models.CharField(max_length=15, choices=ROLES, default='cliente')
    telefono = models.CharField(max_length=15, blank=True, null=True)

    REQUIRED_FIELDS = ['rol', 'email']