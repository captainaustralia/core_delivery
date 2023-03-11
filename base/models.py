from django.db import models

from core_delivery.base.choices import GenderType, TransportType
from core_delivery.basemodel import BaseModel


class PassportData(BaseModel):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    middle_name = models.CharField(max_length=50, verbose_name="Отчество")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    date_of_birth = models.DateField(verbose_name="Дата рождения")
    place_of_birth = models.CharField(max_length=200, verbose_name="Место рождения")
    gender = models.PositiveSmallIntegerField(choices=GenderType.choices)
    series = models.CharField(max_length=4, verbose_name="Серия паспорта")
    number = models.CharField(max_length=6, verbose_name="Номер паспорта")
    expired_date = models.DateField(verbose_name="Дата истечения паспорта")
    verify = models.BooleanField(default=False, verbose_name="Паспорт верифицирован")
    checking_worker = models.ForeignKey(
        "users.DefaultUser",
        null=True,
        on_delete=models.DO_NOTHING,
        editable=False,
        verbose_name="Ответственный сотрудник",
    )

    class Meta:
        verbose_name = "Паспортные данные"
        verbose_name_plural = "Паспортные данные"


class Transport(BaseModel):
    available_weight = models.PositiveIntegerField(verbose_name="Максимальный вес")
    available_volume = models.PositiveIntegerField(verbose_name="Максимальный объем")
    transport_type = models.PositiveSmallIntegerField(choices=TransportType.choices)
    registration_number = models.CharField(
        max_length=8, default="", verbose_name="Регистрационные номера"
    )

    class Meta:
        verbose_name = "Транспорт доставщика"
        verbose_name_plural = "Транспорт доставщиков"
