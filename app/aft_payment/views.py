from django.shortcuts import render
from rest_framework import viewsets

import africastalking

from aft_payment.models import (
    Bank,
    BankTransfer,
    BusinessToBusiness,
    BusinessToCustomer,
    CardCheckout,
    CustomerToBusiness,
    TopupStash,
    WalletTransfer,
)
from aft_payment.serializers import (
    BankSerializer,
    BTResponseEntrySerializer,
    BTRecipientSerializer,
    BankTransferSerializer,
    BusinessToBusinessSerializer,
    BusinessToCustomerSerializer,
    CardCheckoutSerializer,
    CustomerToBusinessSerializer,
    TopupStashSerializer,
    WalletTransferSerializer,
    CardSerializer
)

# Create your views here.


class CustomerToBusinessViewSet(viewsets.ModelViewSet):
    queryset = CustomerToBusiness.objects.all()
    serializer_class = CustomerToBusinessSerializer


class BusinessToCustomerViewSet(viewsets.ModelViewSet):
    queryset = BusinessToCustomer.objects.all()
    serializer_class = BusinessToCustomerSerializer


class BusinessToBusinessViewSet(viewsets.ModelViewSet):
    queryset = BusinessToBusiness.objects.all()
    serializer_class = BusinessToBusinessSerializer


class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class BankTransferViewSet(viewsets.ModelViewSet):
    queryset = BankTransfer.objects.all()
    serializer_class = BankTransferSerializer
    
    def create(self, request, *args, **kwargs):
        bank_transfer = africastalking.Payment
        
        response = bank_transfer.bank_transfer(
            request.data['product_name'],
            request.data['recipients']
        )
        
        rpt_list = []
        
        for recipient in request.data['recipients']:
            bank_detail = recipient['bank_account']
            bank_detail["bank_account_name"] = bank_detail.get('account_name', None)
            bank_detail['bank_account_no'] = bank_detail['account_number']
            bank_detail['bank_account_code'] = bank_detail['bank_code']
            bank_detail['bank_account_DOB'] = bank_detail.get('DOB', None)
            bank_detail['currency_code'] = recipient['currency_code']
            bank_detail['amount'] = recipient['amount']
            bank_detail['narration'] = recipient['narration']
            bank_detail['metadata'] = recipient.get('metadata', None)
            
            bt_recipient = BTRecipientSerializer(data=bank_detail)
            bt_recipient.is_valid()
            instance = btr_serializer.save()
            rpt_list.append(instance.id)
            
        
        entries_list = []
        
        for entry in response['entries']:
            entry['account_number'] = entry.pop('accountNumber')
            entry['transaction_id'] = entry.pop('transactionId')
            entry['transaction_fee'] = entry.pop('transactionFee')
            entry['error_message'] = entry.pop('errorMessage')
            
            btr_serializer = BTResponseEntrySerializer(data=entry)
            btr_serializer.is_valid()
            instance = btr_serializer.save()
            entries_list.append(instance.id)
        
        
        entries_list = []
        
        for entry in response['entries']:
            entry['account_number'] = entry.pop('accountNumber')
            entry['transaction_id'] = entry.pop('transactionId')
            entry['transaction_fee'] = entry.pop('transactionFee')
            entry['error_message'] = entry.pop('errorMessage')
            
            btr_serializer = BTResponseEntrySerializer(data=entry)
            btr_serializer.is_valid()
            instance = btr_serializer.save()
            entries_list.append(instance.id)
        
        request.data['entries'] = entries_list
        request.data['error_message'] = response.get("error_message", None)
        
        return super().create(request, *args, **kwargs)


class CardCheckoutViewSet(viewsets.ModelViewSet):
    queryset = CardCheckout.objects.all()
    serializer_class = CardCheckoutSerializer
    
    def create(self, request, *args, **kwargs):
        card_checkout = africastalking.Payment
        payment_card =  request.data.get('payment_card', None),
        
        response = card_checkout.card_checkout(
            request.data['product_name'],
            request.data['currency_code'],
            request.data['amount'],
            payment_card[0],
            request.data.get('checkout_token', None),
            request.data['narration'],
            request.data.get('metadata', {})
        )
        
        request.data['status'] = response['status']
        request.data['description'] = response['description']
        request.data['transaction_id'] = response.get("transactionId", None)
        
        if (payment_card is not None) :
            card_serializer = CardSerializer(data=payment_card[0])
            card_serializer.is_valid()
            instance = card_serializer.save()
            request.data['payment_card'] = instance.id
    
        
        return super().create(request, *args, **kwargs)

class WalletTransferViewSet(viewsets.ModelViewSet):
    queryset = WalletTransfer.objects.all()
    serializer_class = WalletTransferSerializer


class TopupStashViewSet(viewsets.ModelViewSet):
    queryset = TopupStash.objects.all()
    serializer_class = TopupStashSerializer
