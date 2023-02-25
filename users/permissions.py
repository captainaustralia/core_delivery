from typing import TYPE_CHECKING

from rest_framework.permissions import BasePermission

if TYPE_CHECKING:
    from django.views import View
    from rest_framework.request import Request

    from core_delivery.users.models import DefaultUser, DeliveryMan


class OwnerOrSuperUserPermission(BasePermission):
    def has_object_permission(
        self, request: "Request", view: "View", obj: "DefaultUser"
    ) -> bool:
        if request.user == obj:
            return True


class OnlyAdminPermission(BasePermission):
    def has_object_permission(
        self, request: "Request", view: "View", obj: "DefaultUser"
    ) -> bool:
        return request.user.is_admin or request.user.is_superuser


class OwnerDeliveryManPermission(BasePermission):
    def has_object_permission(
        self, request: "Request", view: "View", obj: "DeliveryMan"
    ) -> bool:
        if request.user.deliveryman == obj:
            return True
