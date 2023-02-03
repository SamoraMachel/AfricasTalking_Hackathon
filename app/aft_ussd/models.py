from django.db import models

from django.urls import reverse
from django.utils.translation import gettext_lazy as _

# Create your models here.
class USSD(models.Model):
    session_id = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    network_code = models.CharField(max_length=100, null=True, blank=True)
    service_code = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    

    class Meta:
        verbose_name = _("ussd")
        verbose_name_plural = _("ussds")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ussd_detail", kwargs={"pk": self.pk})
