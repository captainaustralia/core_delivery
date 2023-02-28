from rest_framework import serializers

from core_delivery.orders.models import Order, Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        exclude = ("date_modified", "deleted")


class OrderWriteSerializer(serializers.ModelSerializer):
    dispatch_point = LocationSerializer()
    delivery_point = LocationSerializer()

    class Meta:
        model = Order
        fields = (
            "content",
            "description",
            "dispatch_point",
            "delivery_point",
            "fragile",
            "weight",
            "dimension",
        )
