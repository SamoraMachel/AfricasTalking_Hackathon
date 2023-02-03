from rest_framework import viewsets

from aft_sms.models import BulkRecipient, BulkSMS
from aft_sms.serializers import (
    BulkRecipientSerializer,
    BulkSMSSerializer,
)

# Create your views here.
class BulkRecipientViewSet(viewsets.ModelViewSet):
    queryset = BulkRecipient.objects.all()
    serializer_class = BulkRecipientSerializer


class BulkSMSViewSet(viewsets.ModelViewSet):
    queryset = BulkSMS.objects.all()
    serializer_class = BulkSMSSerializer
