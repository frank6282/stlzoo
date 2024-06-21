from django.db import models


# Create your models here.
class Suppliers(models.Model):
    name = models.CharField(max_length=60, null=True, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zipcode = models.CharField(max_length=15, null=True, blank=True)

    def save(self, *args, **kwargs):
        supplier_id = id

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Supplier"
        ordering = ("name",)

    def __str__(self):
        return f"{self.name}"
