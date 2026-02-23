from rest_framework import routers
from .views import UsuarioViewSet

router = routers.DefaultRouter()

router.register('usuarios', UsuarioViewSet)

urlpatterns = router.urls