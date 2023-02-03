from django.shortcuts import render
from rest_framework import viewsets

from aft_ussd.models import USSD, UserReg
from aft_ussd.serializers import UserRegSerializer, USSDSerializer
from aft_sms.serializers import (
    BulkRecipientSerializer,
    BulkSMSSerializer,
)

from rest_framework import status
from rest_framework.response import Response
# Create your views here.


class USSDViewSet(viewsets.ModelViewSet):
    queryset = USSD.objects.all()
    serializer_class = USSDSerializer

    # def create(self, request, *args, **kwargs):
    #     if request.data["text"] == "":
    #         response = "CON Starting Registration.\n Please Insert your name"

    #     return super().create(request, *args, **kwargs)


class UserRegViewSet(viewsets.ModelViewSet):
    queryset = UserReg.objects.all()
    serializer_class = UserRegSerializer


class UpdateUsers(viewsets.ModelViewSet):
    queryset = UserReg.objects.all()
    serializer_class = UserRegSerializer
    
    def create(self, request, *args, **kwargs):
        import africastalking
        user_name  = request.data['username']
        user_loc = request.data['location']
        
        queryst = UserReg.objects.filter(location=user_loc)
        phoneNumber = ""
        for item in queryst: 
            phoneNumber += f"{item.phone_number},"
        
        phoneNoList = phoneNumber.split(',')
        phoneNoList.pop()
         
        sms = africastalking.SMS
        response = sms.send(
            f"Alert {user_name} is in danger",
            phoneNoList,
            request.data.get("short_code", None),
        )
        
        request.data['response_message'] = response['SMSMessageData']['Message']
        rcpts_list = []
        
        for recipients in response['SMSMessageData']['Recipients']:
            print(recipients)
            recipients['status_code'] = recipients.pop('statusCode')
            recipients['message_id'] = recipients.pop('messageId')
            recpt_serializer = BulkRecipientSerializer(data=recipients)
            recpt_serializer.is_valid()
            instance = recpt_serializer.save()
            rcpts_list.append(instance.id)
        
        request.data['response_recipients'] = rcpts_list       
        
        return Response("Successfully sent", status=status.HTTP_200_OK)