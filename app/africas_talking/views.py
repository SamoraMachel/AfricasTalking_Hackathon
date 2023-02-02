from django.shortcuts import render

from africas_talking.models import RecievedSMS, SentSMS
from africas_talking.serializers import RecievedSMSSerializer, SentSMSSerializer


# Create your views here.


class SentSMSViewSet(viewsets.ModelViewSet):
    queryset = SentSMS.objects.all()
    serializer_class = SentSMSSerializer


class RecievedSMSViewSet(viewsets.ModelViewSet):
    queryset = RecievedSMS.objects.all()
    serializer_class = RecievedSMSSerializer
