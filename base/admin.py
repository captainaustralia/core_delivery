from django import apps
from django.contrib import admin

# Register your models here.
models = apps.apps.get_models()[5:]
for model in models:
    admin.site.register(model)
