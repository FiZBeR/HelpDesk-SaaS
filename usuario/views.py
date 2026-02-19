from rest_framework import viewsets, permissions
from .models import UsuarioModel
from .serializer import UsuarioSerializer
# Create your views here.

class UsuarioViewSet (viewsets.ModelViewSet):
    queryset = UsuarioModel.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        return UsuarioModel.objects.all()