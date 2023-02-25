from rest_framework import serializers

from core_delivery.orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "content",
            "description",
            "dispatch_point",
            "delivery_point",
            "fragile",
            "weight",
            "dimension"
        )
