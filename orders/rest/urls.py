from rest_framework.routers import SimpleRouter

from core_delivery.orders.rest.views import OrderViewSet

router = SimpleRouter()
router.register(basename="order", viewset=OrderViewSet, prefix="")

urlpatterns = [] + router.urls
