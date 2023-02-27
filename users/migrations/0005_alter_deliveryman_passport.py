# Generated by Django 4.1.7 on 2023-02-25 14:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0004_remove_transport_owner"),
        ("users", "0004_deliveryman_verified_alter_defaultuser_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="deliveryman",
            name="passport",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="deliveryman",
                to="base.passportdata",
                verbose_name="Паспортные данные",
            ),
        ),
    ]