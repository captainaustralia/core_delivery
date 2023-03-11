from rest_framework.routers import SimpleRouter

from core_delivery.base.rest.views import PassportDataReadOnlyViewSet

router = SimpleRouter()
router.register("passports", PassportDataReadOnlyViewSet, "passports")

urlpatterns = [] + router.urls
