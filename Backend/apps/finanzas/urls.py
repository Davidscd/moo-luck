from rest_framework.routers import DefaultRouter
from .views import CategoriaGastoViewSet, TransaccionViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaGastoViewSet, basename='categoria-gasto')
router.register(r'transacciones', TransaccionViewSet, basename='transaccion')

urlpatterns = router.urls
