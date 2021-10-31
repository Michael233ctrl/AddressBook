from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=200, unique=True)
    last_name = models.CharField(max_length=200, unique=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
