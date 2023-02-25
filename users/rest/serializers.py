from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from core_delivery.users import models as us_mod


class DefaultUserSerializer(ModelSerializer):
    class Meta:
        model = us_mod.DefaultUser
        fields = (
            "email",
            "uuid",
            "first_name",
            "middle_name",
            "last_name",
            "age",
            "phone",
            "password",
        )
        read_only_fields = ("uuid",)
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {"write_only": True},
            "phone": {"write_only": True},
        }

    @staticmethod
    def validate_password(password):
        if len(password) < 10:
            raise serializers.ValidationError("Password length must be > 10")

    def create(self, validated_data):
        return us_mod.DefaultUser.objects.create_user(**validated_data)


class DeliveryManSerializer(ModelSerializer):
    user = DefaultUserSerializer(read_only=True)

    class Meta:
        model = us_mod.DeliveryMan
        fields = ("uuid", "user", "transport", "passport")
        read_only_fields = ("uuid",)
        extra_kwargs = {"passport": {"write_only": True}}
