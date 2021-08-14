from django.core.cache import cache
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.api.serializers import VehicleSerializers
from apps.car.models import Vehicle


class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializers
    queryset = Vehicle.objects.filter(is_active=True).select_related('vehicle_model')
    authentication_classes = BasicAuthentication,
    permission_classes = IsAuthenticated,

    @staticmethod
    def get_cache_key(pk):
        return f'vehicle_{pk}'

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        cache_key = self.get_cache_key(pk)
        if not cache.get(cache_key):
            response = super().retrieve(request, *args, **kwargs)
            cache.set(cache_key, response.data)
        return Response(cache.get(cache_key))

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        pk = kwargs.get('pk')
        cache_key = self.get_cache_key(pk)
        cache.set(cache_key, response.data)
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        pk = kwargs.get('pk')
        cache_key = self.get_cache_key(pk)
        cache.set(cache_key, response.data)
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        pk = kwargs.get('pk')
        cache_key = self.get_cache_key(pk)
        cache.delete(cache_key)
        return response
