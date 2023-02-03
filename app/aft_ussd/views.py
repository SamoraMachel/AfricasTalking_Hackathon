from django.shortcuts import render

from aft_ussd.models import USSD
from aft_ussd.serializers import USSDSerializer

from rest_framework import viewsets

# Create your views here.


class USSDViewSet(viewsets.ModelViewSet):
    queryset = USSD.objects.all()
    serializer_class = USSDSerializer

    def create(self, request, *args, **kwargs):
        if request.data['text'] == '':
            response = "CON Starting Registration.\n Please Insert your name"
        
        return super().create(request, *args, **kwargs)