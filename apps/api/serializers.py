from rest_framework import serializers

from apps.car.models import Vehicle, VehicleModel


class VehicleModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = ('name', 'brand', 'id')


class VehicleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('vehicle_model', 'vehicle_model_id', 'id', 'plaka', 'km', 'sase_no', 'renk')

    vehicle_model = VehicleModelSerializers(many=False, read_only=True)
    vehicle_model_id = serializers.IntegerField(required=True, write_only=True)


