from django.urls import include, path
from rest_framework import routers

from aft_ussd.views import UserRegViewSet, USSDViewSet, UpdateUsers

router = routers.DefaultRouter()
router.register(r"ussd", USSDViewSet)

router.register(r"userregs", UserRegViewSet)
router.register(r'updateUsers', UpdateUsers)

urlpatterns = [
    path("", include(router.urls)),
]
