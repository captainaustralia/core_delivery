from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from core_delivery.base.models import PassportData, Transport
from core_delivery.basemodel import BaseModel, BaseUser


class DefaultUser(BaseUser):
    first_name = models.CharField(max_length=50, verbose_name="Имя пользователя")
    middle_name = models.CharField(
        max_length=50, verbose_name="Отчество пользователя", default=""
    )
    last_name = models.CharField(max_length=50, verbose_name="Фамилия пользователя")
    age = models.PositiveIntegerField(verbose_name="Возраст пользователя", default=0)
    phone = PhoneNumberField(
        region="RU", db_index=True, verbose_name="Номер телефона"  # ISO_3166-1
    )
    verify = models.BooleanField(
        default=False, verbose_name="Пользователь верифицирован"
    )

    def make_verify(self):
        if self.verify:
            return
        self.verify = True
        self.save()

    @property
    def is_deliveryman(self):
        return self.deliveryman

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class DeliveryMan(BaseModel):
    user = models.OneToOneField(
        DefaultUser,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="deliveryman",
    )

    passport = models.OneToOneField(
        PassportData,
        on_delete=models.DO_NOTHING,
        verbose_name="Паспортные данные",
        related_name="deliveryman",
        null=True,
    )

    transport = models.OneToOneField(
        Transport,
        null=True,
        on_delete=models.SET_NULL,
        related_name="deliveryman",
        verbose_name="Транспортное средство доставщика",
    )

    verified = models.BooleanField(
        default=False, verbose_name="Доставщик верифицирован"
    )

    class Meta:
        verbose_name = "Доставщик"
        verbose_name_plural = "Доставщики"
