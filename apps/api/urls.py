from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from apps.api.views import VehicleViewSet

router = routers.DefaultRouter()
router.register(r'vehicle', VehicleViewSet)

urlpatterns = [
    url(r'', include(router.urls))
]