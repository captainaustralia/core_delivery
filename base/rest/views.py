from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from core_delivery.base.rest.serializers import OrderSerializer
from core_delivery.orders.models import Order


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = (permissions.AllowAny,)
