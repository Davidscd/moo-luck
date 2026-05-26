from rest_framework.routers import DefaultRouter
from .views import EventoSanitarioViewSet

router = DefaultRouter()
router.register(r'', EventoSanitarioViewSet, basename='evento-sanitario')

urlpatterns = router.urls
