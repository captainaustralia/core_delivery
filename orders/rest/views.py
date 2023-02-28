from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from core_delivery.orders.models import Order
from core_delivery.orders.rest.serializers import OrderWriteSerializer


class OrderViewSet(ModelViewSet):
    serializer_class = OrderWriteSerializer
    queryset = Order.objects.all()
    permission_classes = (permissions.AllowAny,)

    @action(url_name="take_order", methods=["get"], detail=True)
    def deliveryman_take_order(self, request):
        deliveryman = request.user.deliveryman
        order = self.get_object()
        order.delivery_man = deliveryman
        order.save()
