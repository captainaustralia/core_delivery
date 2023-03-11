import datetime
from typing import Optional

from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from core_delivery.base.models import PassportData, Transport


class PassportDataSerializer(ModelSerializer):
    class Meta:
        model = PassportData
        exclude = ("date_modified", "date_created", "deleted")
        read_only_fields = ("verify",)

    @staticmethod
    def validate_expired_date(date) -> Optional[datetime.datetime]:
        if date + datetime.timedelta(days=30) >= datetime.datetime.now().date():
            raise ValidationError("Document was expired, or expire within 30 days!")
        return date

    @staticmethod
    def validate_date_of_birth(date: datetime.datetime) -> Optional[datetime.datetime]:
        if datetime.datetime.now().year - date.year < 0:
            raise ValidationError("You must be of legal age")
        return date


class TransportSerializer(ModelSerializer):
    class Meta:
        model = Transport
        exclude = ("date_modified", "date_created", "deleted")
