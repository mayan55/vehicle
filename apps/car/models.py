from django.db import models
from apps.core.models import BaseModel


class VehicleModel(BaseModel):
    brand = models.CharField("brand", max_length=100)
    name = models.CharField("name", max_length=100)

    def __str__(self):
        return "{} {}".format(self.brand, self.name)


class Vehicle(BaseModel):
    vehicle_model = models.ForeignKey(VehicleModel, on_delete=models.SET_NULL, null=True)
    plaka = models.CharField("PLAKA", max_length=12)
    km = models.IntegerField("KM", default=0)
    sase_no = models.CharField("SASENO", max_length=100)
    renk = models.CharField("RENK", max_length=24)
