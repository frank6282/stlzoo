from django.db import models


# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    e_mail = models.EmailField(max_length=250)
    phone_number = models.CharField(max_length=15)
    contact_message = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.first_name + " " + self.last_name)
