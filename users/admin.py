from django.contrib import admin

from core_delivery.users.models import DefaultUser, DeliveryMan

# Register your models here.
admin.site.register(DefaultUser)
admin.site.register(DeliveryMan)
