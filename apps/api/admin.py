from django.contrib import admin

# Register your models here.
from apps.car.models import VehicleModel

admin.site.register(VehicleModel)