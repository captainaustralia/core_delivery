from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from core_delivery.base.models import PassportData
from core_delivery.base.rest.serializers import PassportDataSerializer


class PassportDataReadOnlyViewSet(ReadOnlyModelViewSet):
    serializer_class = PassportDataSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)
    queryset = PassportData.objects.all()

    @action(methods=["get"], detail=True)
    def verify(self, request, **kwargs):
        passport_obj: PassportData = self.get_object()
        if passport_obj.verify:
            return Response(status=200, data="Passport already verified!")

        passport_obj.verify = True
        passport_obj.checking_worker = self.request.user
        passport_obj.save()

        return Response(status=200, data="Passport checked!")
