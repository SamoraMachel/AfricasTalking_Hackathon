from django.urls import include, path
from rest_framework import routers

from africas_talking.views import RecievedSMSViewSet, SentSMSViewSet

router = routers.DefaultRouter()
router.register(r"sentsm", SentSMSViewSet)
router.register(r"recievedsm", RecievedSMSViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
