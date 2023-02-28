import datetime

from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from core_delivery.base.models import PassportData


class PassportDataSerializer(ModelSerializer):
    class Meta:
        model = PassportData
        exclude = ('date_modified', 'date_created', 'deleted')
        read_only_fields = ('verify',)

    @staticmethod
    def validate_expired_date(date):
        print(date, datetime.datetime.now().date())
        if date + datetime.timedelta(days=30) >= datetime.datetime.now().date():
            raise ValidationError("Document was expired, or expire within 30 days!")
        return date

    @staticmethod
    def validate_date_of_birth(date: datetime.datetime):
        print(date.year, datetime.datetime.now().year)
        if datetime.datetime.now().year - date.year < 0:
            raise ValidationError("You must be of legal age")
        return date
