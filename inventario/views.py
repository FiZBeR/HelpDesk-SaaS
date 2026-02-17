from rest_framework import viewsets, permissions
from .models import EquipoModel
from .serializer import EquipoSerializer

# Create your views here.
class EquipoViewSet (viewsets.ModelViewSet):
    queryset = EquipoModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EquipoSerializer

    def perform_destroy(self, instance):
        instance.estado = 'dado_de_baja'
        instance.save()