from rest_framework import routers
from .views import EquipoViewSet

router = routers.DefaultRouter()

router.register('equipos', EquipoViewSet)

urlpatterns = router.urls