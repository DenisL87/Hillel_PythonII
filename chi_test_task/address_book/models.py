from django.db import models


# class Address(models.Model):
#     country = models.CharField(max_length=125)
#     city = models.CharField(max_length=125)
#     street = models.CharField(max_length=125)


class Person(models.Model):
    first_name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=125)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    url = models.URLField(blank=True)
