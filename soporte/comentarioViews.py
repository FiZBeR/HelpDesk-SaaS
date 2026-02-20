from rest_framework import viewsets, permissions
from .models import ComentarioModel
from .serializer import ComentarioSerializer

class ComentarioViewset (viewsets.ModelViewSet):
    queryset = ComentarioModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ComentarioSerializer

    def perform_create(self, serializer):
        serializer.save(autor = self.request.user)

    def get_queryset(self):
        user = self.request.user
        queryset = ComentarioModel.objects.all()

        if user == 'cliente':
            return queryset.filter(es_interno = False)

        return queryset
        