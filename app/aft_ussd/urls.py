from django.urls import include, path
from rest_framework import routers

from aft_ussd.views import USSDViewSet

router = routers.DefaultRouter()
router.register(r"ussd", USSDViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
