from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core_delivery.users.exceptions import AlreadyDeliveryException
from core_delivery.users.models import DefaultUser, DeliveryMan
from core_delivery.users.permissions import (
    OnlyAdminPermission,
    OwnerDeliveryManPermission,
    OwnerOrSuperUserPermission,
)
from core_delivery.users.rest.serializers import (
    DefaultUserSerializer,
    DeliveryManSerializer,
)


class DefaultUserViewSet(ModelViewSet):
    http_method_names = ("get", "post", "patch", "delete")
    serializer_class = DefaultUserSerializer
    queryset = DefaultUser.objects.all()
    permission_classes = (permissions.AllowAny,)

    def list(self, request, *args, **kwargs):
        self.permission_classes = (
            permissions.IsAuthenticated,
        )
        return super().list(request, args, kwargs)

    def update(self, request, *args, **kwargs) -> DefaultUser:
        self.permission_classes = (
            permissions.IsAuthenticated,
            OwnerOrSuperUserPermission,
        )
        return super().update(request, args, kwargs)

    def destroy(self, request, *args, **kwargs) -> Response:
        self.permission_classes = (
            permissions.IsAuthenticated,
            OwnerOrSuperUserPermission,
        )
        return super().destroy(request, args, kwargs)

    @action(methods=["get"], detail=True, permission_classes=[permissions.IsAuthenticated, OnlyAdminPermission])
    def verify(self, request: Request, pk) -> Response:
        obj: DefaultUser = self.get_object()
        obj.make_verify()
        return Response(status=200, data=f"Success verify! {obj.email}, {pk}")


class DeliveryManViewSet(ModelViewSet):
    http_method_names = ("get", "post")
    serializer_class = DeliveryManSerializer
    permission_classes = (permissions.IsAuthenticated, OwnerDeliveryManPermission)

    queryset = DeliveryMan.objects.select_related("user", "passport", "transport").all()

    def perform_create(self, serializer):
        user = self.request.user
        if self._is_user_already_delivery_man(user):
            raise AlreadyDeliveryException
        serializer.save(user=user)

    @staticmethod
    def _is_user_already_delivery_man(user):
        return hasattr(user, "deliveryman")

    # @action(methods=["post"])
    # def add_transport(self):
    #     ...
    #
    # @action(methods=["post"])
    # def add_passport(self):
    #     ...
