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
    # id = serializers.IntegerField(read_only=True)
    # plaka = serializers.CharField(required=True, max_length=12)
    # km = serializers.IntegerField(required=True)
    # sase_no = serializers.CharField(required=True, max_length=100)
    # renk = serializers.CharField(required=True, max_length=24)

    # def create(self, validated_data):
    #     return Vehicle.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     for field, value in validated_data.items():
    #         setattr(instance, field, value)
    #     instance.save()
    #     return instance

