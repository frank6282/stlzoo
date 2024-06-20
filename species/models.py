from django.db import models


# Create your models here.
class Species(models.Model):
    scientific_name = models.CharField(max_length=50)
    common_name = models.CharField(max_length=50, null=True, blank=True)
    butterfly_image = models.ImageField(
        null=True, blank=True, upload_to="images/", default="images/default.png"
    )
    description = models.TextField(
        max_length=1000, null=True, blank=True, default="none"
    )

    def __str__(self):
        return self.scientific_name

    class Meta:
        verbose_name = "Specie"
        ordering = ["scientific_name"]
