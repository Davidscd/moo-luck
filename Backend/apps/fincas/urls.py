from rest_framework.routers import DefaultRouter
from .views import FincaViewSet

router = DefaultRouter()
router.register(r'', FincaViewSet, basename='finca')

urlpatterns = router.urls
