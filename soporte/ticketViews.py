from rest_framework import viewsets, permissions, status
from .models import TicketModel
from .serializer import TicketSerializer, ComentarioSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone

# Create your views here.
class TicketViewSet (viewsets.ModelViewSet):
    queryset = TicketModel.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TicketSerializer

    def perform_create(self, serializer):
        cliente = self.request.user
        
        serializer.save(cliente = cliente)
    
    @action(detail=True, methods=['POST'])
    def resolver_ticket(self, request, pk=None):
        objeto = self.get_object()

        if not objeto.comentarios.exists():
            return Response(
                {'error': 'No se puede resolver un ticket que no tiene evidencia o comentarios de soporte.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Si ya está resuelto, no hacemos nada
        if objeto.estado == 'resuelto':
            return Response(
                {'error': 'El ticket ya se encuentra en estado resuelto.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        objeto.estado = 'resuelto'
        objeto.fecha_cierre = timezone.now()

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
                'tickets_abiertos' : abiertos,
                'tickets_en_progreso' : en_progreso,
                'tickets_resueltos' : resueltos
            },
            status = status.HTTP_200_OK
        )

    @action(detail=True, methods=['get'])
    def comentarios(self, request, pk=None):
        ticket = self.get_object()
        # Usamos el related_name que definimos en el modelo
        comentarios = ticket.comentarios.all().order_by('-fecha')
        
        serializer = ComentarioSerializer(comentarios, many=True)
        return Response(serializer.data)