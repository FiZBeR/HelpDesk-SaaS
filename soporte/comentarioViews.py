from rest_framework import viewsets, permissions
from .models import ComentarioModel
from .serializer import ComentarioSerializer

class ComentarioViewset (viewsets.ModelViewSet):
    queryset = ComentarioModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ComentarioSerializer