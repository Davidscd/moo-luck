from rest_framework.routers import DefaultRouter
from .views import PesajeViewSet

router = DefaultRouter()
router.register(r'', PesajeViewSet, basename='pesaje')

urlpatterns = router.urls
