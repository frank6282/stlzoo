from django.db import models

# Create your models here.
from suppliers.models import Suppliers
from species.models import Species


# Create your models here.
class Shipments(models.Model):
    yes_no_choice = ((True, "Yes"), (False, "No"))

    supplier = models.ForeignKey(
        Suppliers,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="supplier",
    )
    species = models.ForeignKey(
        Species,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="species",
    )
    label = models.CharField(max_length=20)
    received = models.PositiveSmallIntegerField(default=0)
    bad = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    non = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    doa = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    para = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    released = models.PositiveSmallIntegerField(
        default=0, blank=True, null=True, editable=False
    )
    entered = models.BooleanField(choices=yes_no_choice, default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        sub_quantity = self.bad + self.non + self.doa + self.para
        self.released = self.received - sub_quantity

        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.supplier)

    class Meta:
        ordering = ["-created"]
