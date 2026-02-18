from rest_framework import routers
from .ticketViews import TicketViewSet
from .comentarioViews import ComentarioViewset

router = routers.DefaultRouter()

router.register('tickets', TicketViewSet)
router.register('comentarios', ComentarioViewset)

urlpatterns = router.urls