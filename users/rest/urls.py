from rest_framework.routers import SimpleRouter

from core_delivery.users.rest.views import DefaultUserViewSet, DeliveryManViewSet

router = SimpleRouter()
router.register(basename="users", viewset=DefaultUserViewSet, prefix="users")
router.register(
    basename="deliveryman", viewset=DeliveryManViewSet, prefix="deliveryman"
)

urlpatterns = [] + router.urls
