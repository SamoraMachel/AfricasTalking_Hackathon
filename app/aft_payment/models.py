from django.db import models

# Create your models here.
class CustomerToBusiness(models.Model):

    

    class Meta:
        verbose_name = _("C2B")
        verbose_name_plural = _("C2B")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("C2B_detail", kwargs={"pk": self.pk})
