from rest_framework import viewsets, permissions, status
from .models import TicketModel
from .serializer import TicketSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class TicketViewSet (viewsets.ModelViewSet):
    queryset = TicketModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TicketSerializer

    def perform_create(self, serializer):
        #Generacón de Codigo - TK-YYYY-XXXX
        return super().perform_create(serializer)
    
    @action(detail=True, methods=['POST'])
    def resoler_ticket(self, request, pk=None):
        objeto = self.get_object()
        objeto.estado = 'resuelto'

        objeto.save()

        return Response(
            {'message' : 'ticket resuleto con exito'},
            status = status.HTTP_200_OK
        ) 
    
    @action(detail=False, methods=['GET'])
    def estadisticas(self, request):
        queryset = self.get_queryset()

        abiertos = queryset.filter(estado = 'abierto').count()
        en_progreso = queryset.filter(estado = 'en_progreso').count()
        resueltos = queryset.filter(estado = 'resuelto').count()

        return Response(
            {
                'Tickets abiertos' : abiertos,
                'Tickets en progreso' : en_progreso,
                'Tickets resueltos' : resueltos
            },
            status = status.HTTP_200_OK
        )