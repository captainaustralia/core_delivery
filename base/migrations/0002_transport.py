# Generated by Django 4.1.7 on 2023-02-25 12:43

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transport",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        db_index=True,
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("date_modified", models.DateTimeField()),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("deleted", models.BooleanField(default=False)),
                (
                    "available_weight",
                    models.PositiveIntegerField(verbose_name="Максимальный вес"),
                ),
                (
                    "available_volume",
                    models.PositiveIntegerField(verbose_name="Максимальный объем"),
                ),
                ("transport_type", models.PositiveSmallIntegerField(choices=[])),
                (
                    "registration_number",
                    models.CharField(
                        default="", max_length=8, verbose_name="Регистрационные номера"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
