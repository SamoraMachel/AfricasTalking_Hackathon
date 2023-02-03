from rest_framework import serializers

from aft_ussd.models import USSD, UserReg


class USSDSerializer(serializers.ModelSerializer):
    class Meta:
        model = USSD
        fields = "__all__"


class UserRegSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReg
        fields = "__all__"
