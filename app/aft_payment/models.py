from django.db import models

from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.
TRANS_STATUS = {
    ('Queued', 'Queued'),
    ('InvalidRequest', 'InvalidRequest'),
    ('NotSupported', 'NotSupported'),
    ('Failed', 'Failed')
}


class CustomerToBusiness(models.Model):
    request_status = {
        ('PendingConfirmation', 'PendingConfirmation'),
        ('InvalidRequest', 'InvalidRequest'),
        ('NotSupported', 'NotSupported'),
        ('Failed', 'Failed')
    }
    
    product_name = models.CharField(max_length=100)
    provider_channel = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.IntegerField()
    currency_code = models.CharField(max_length=5)
    amount = models.DecimalField()
    metadata = models.JSONField(null=True, blank=True)
    
    # Response
    status = models.CharField(max_length=30, choices=request_status, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    provider = models.CharField(max_length=50, null=True, blank=True)
    

    class Meta:
        verbose_name = _("C2B")
        verbose_name_plural = _("C2B")

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse("C2B_detail", kwargs={"pk": self.pk})


class B2CRecipient(models.Model):
    reason_choice = {
            ("SalaryPayment", "SalaryPayment"),
            ("SalaryPaymentWithWithdrawalChargePaid", "SalaryPaymentWithWithdrawalChargePaid"),
            ("BusinessPayment", "BusinessPayment"),
            ("BusinessPaymentWithWithdrawalChargePaid", "BusinessPaymentWithWithdrawalChargePaid"),
            ("PromotionPayment", "PromotionPayment"),
    }
    
    name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=50)
    currency = models.CharField(max_length=5)
    amount = models.DecimalField()
    provider_channel = models.CharField(max_length=100, null=True, blank=True)
    reason = models.CharField(max_length=50, choices=reason_choice, null=True, blank=True)
    metadata = models.JSONField(null=True, blank=True)
    

    class Meta:
        verbose_name = _("B2CRecipient")
        verbose_name_plural = _("B2CRecipients")

    def __str__(self):
        return self.phone_number

    def get_absolute_url(self):
        return reverse("B2CRecipient_detail", kwargs={"pk": self.pk})

class B2CEntries(models.Model):
    phone_number = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=TRANS_STATUS)
    transaction_id = models.CharField(max_length=50, null=True, blank=True)
    provider = models.CharField(max_length=50, null=True, blank=True)
    provider_channel = models.CharField(max_length=50, null=True, blank=True)
    value = models.CharField(max_length=150, null=True, blank=True)
    transaction_fee = models.CharField(max_length=100, null=True, blank=True)
    error_message = models.CharField(max_length=250, null=True, blank=True)
    

    class Meta:
        verbose_name = _("B2CEntries")
        verbose_name_plural = _("B2CEntries")

    def __str__(self):
        return self.phone_number

    def get_absolute_url(self):
        return reverse("B2CEntries_detail", kwargs={"pk": self.pk})


class BusinessToCustomer(models.Model):
    product_name = models.CharField(max_length=100)
    recipients = models.ManyToOneRel(B2CRecipient, on_delete=models.CASCADE)
    
    # response
    number_queued = models.IntegerField(null=True, blank=True)
    total_value = models.CharField(max_length=150, null=True, blank=True)
    entries = models.ManyToOneRel(B2CEntries, on_delete=models.CASCADE)
    error_message = models.CharField(max_length=200, null=True, blank=True)
    
    

    class Meta:
        verbose_name = _("B2C")
        verbose_name_plural = _("B2C")

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse("B2C_detail", kwargs={"pk": self.pk})



class BusinessToBusiness(models.Model):
    provider_choices = {
        ('Mpesa', 'Mpesa'),
        ('TigoTanzania', 'TigoTanzania'),
        ('Athena', 'Athena')
    }
    
    product_name = models.CharField(max_length=100)
    provider = models.CharField(max_length=50, choices=provider_choices)
    transfer_type = models.CharField(max_length=100, default="BusinessToBusinessTransfer")
    currency_code = models.CharField(max_length=5)
    amount = models.CharField(max_length=150)
    destination_channel = models.CharField(max_length=100)
    destination_account = models.CharField(max_length=100)
    metadata = models.JSONField(null=True, blank=True)
    
    # response
    status = models.CharField(max_length=30, choices=TRANS_STATUS, null=True, blank=True)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    transaction_fee = models.CharField(max_length=100, null=True, blank=True)
    provider_channel = models.CharField(max_length=50, null=True, blank=True)
    error_message = models.CharField(max_length=100, null=True, blank=True)
    

    class Meta:
        verbose_name = _("B2B")
        verbose_name_plural = _("B2B")

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse("B2B_detail", kwargs={"pk": self.pk})
    
class Bank(models.Model):
    product_name = models.CharField(max_length=100)
    bank_account_name = models.CharField(max_length=100)
    bank_account_no = models.CharField(max_length=50)
    bank_account_code = models.IntegerField()
    bank_account_DOB = models.CharField(max_length=100, null=True, blank=True)
    currency_code = models.CharField(max_length=5)
    amount = models.DecimalField()
    narration = models.CharField(max_length=250)
    metadata = models.JSONField(null=True, blank=True)
    
    # response
    status = models.CharField(max_length=50, choices=TRANS_STATUS, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    transaction_id = models.CharField(max_length=50, null=True, blank=True)
    

    class Meta:
        verbose_name = _("bank")
        verbose_name_plural = _("banks")

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse("bank_detail", kwargs={"pk": self.pk})    \

class BTRecipient(models.Model):
    bank_account_name = models.CharField(max_length=100)
    bank_account_no = models.CharField(max_length=50)
    bank_account_code = models.IntegerField()
    bank_account_DOB = models.CharField(max_length=100, null=True, blank=True)
    currency_code = models.CharField(max_length=5)
    amount = models.DecimalField()
    narration = models.CharField(max_length=250)
    metadata = models.JSONField(null=True, blank=True)

    class Meta:
        verbose_name = _("banktransferrecipient")
        verbose_name_plural = _("banktransferrecipients")

    def __str__(self):
        return self.account_name

    def get_absolute_url(self):
        return reverse("banktransferrecipient_detail", kwargs={"pk": self.pk})

class BTResponseEntry(models.Model):
    account_number = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=TRANS_STATUS)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    transaction_fee = models.CharField(max_length=100, null=True, blank=True)
    error_message = models.CharField(max_length=100, null=True, blank=True)
    

    class Meta:
        verbose_name = _("btresponseentry")
        verbose_name_plural = _("btresponseentrys")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("btresponseentry_detail", kwargs={"pk": self.pk})


class BankTransfer(models.Model):
    product_name = models.CharField(max_length=100)
    recipients = models.ManyToOneRel(BTRecipient, on_delete=models.CASCADE)
    
    # response
    entries = models.ManyToOneRel(BTResponseEntry, on_delete=models.CASCADE)
    error_message = models.CharField(max_length=100, null=True, blank=True)
    
    

    class Meta:
        verbose_name = _("banktransfer")
        verbose_name_plural = _("banktransfers")

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse("banktransfer_detail", kwargs={"pk": self.pk})

class Card(models.Model):
    number = models.CharField(max_length=50)
    cvv_number = models.IntegerField()
    expiry_month = models.IntegerField()
    expiry_year = models.IntegerField()
    country_code = models.CharField(max_length=2)
    auth_token = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = _("card")
        verbose_name_plural = _("cards")

    def __str__(self):
        return self.number

    def get_absolute_url(self):
        return reverse("card_detail", kwargs={"pk": self.pk})



class CardCheckout(models.Model):
    request_status = {
        ("PendingConfirmation", "PendingConfirmation"),
        ("Success", "Success"),
        ("InvalidRequest", "InvalidRequest"),
        ("NotSupported", "NotSupported"),
        ("Failed", "Failed")
    }
    
    product_name = models.CharField(max_length=100)
    payment_card = models.ForeignKey(Card, on_delete=models.CASCADE, null=True, blank=True)
    checkout_token = models.CharField(max_length=150, null=True, blank=True)
    currency_code = models.CharField(max_length=3)
    amount = models.DecimalField()
    narration = models.CharField(max_length=250)
    metadata = models.JSONField(null=True, blank=True)
    
    # response
    status = models.CharField(max_length=50, choices=request_status)
    description = models.CharField(max_length=100)
    transaction_id = models.CharField(max_length=50, null=True, blank=True)
    
    class Meta:
        verbose_name = _("cardcheckout")
        verbose_name_plural = _("cardcheckout")

    def __str__(self):
        return self.prodcut_name

    def get_absolute_url(self):
        return reverse("cardcheckout_detail", kwargs={"pk": self.pk})

class WalletTransfer(models.Model):
    request_status = {
        ("Success", "Success"),
        ("Failed", "Failed")
    }
    
    product_name = models.CharField(max_length=100)
    targetProductCode = models.IntegerField()
    currency_code = models.CharField(max_length=3)
    amount = models.DecimalField()
    metadata = models.JSONField()

    # response
    status = models.CharField(max_length=50, choices=request_status)
    description = models.CharField(max_length=100)
    transaction_id = models.CharField(max_length=50, null=True, blank=True)
    
    class Meta:
        verbose_name = _("wallettransfer")
        verbose_name_plural = _("wallettransfers")

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse("wallettransfer_detail", kwargs={"pk": self.pk})

class TopupStash(models.Model):
    request_status = {
        ("Success", "Success"),
        ("Failed", "Failed")
    }
    
    product_name = models.CharField(max_length=100)
    currency_code = models.CharField(max_length=3)
    amount = models.DecimalField()
    metadata = models.JSONField()

    # response
    status = models.CharField(max_length=50, choices=request_status)
    description = models.CharField(max_length=100)
    transaction_id = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = _("topupstash")
        verbose_name_plural = _("topupstashs")

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse("topupstash_detail", kwargs={"pk": self.pk})

