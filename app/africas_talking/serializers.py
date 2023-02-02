from rest_framework import serializers

from africas_talking.models import RecievedSMS, SentSMS


class SentSMSSerializer(serializers.ModelSerializer):
    class Meta:
        model = SentSMS
        fields = "__all__"


class RecievedSMSSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecievedSMS
        fields = "__all__"
