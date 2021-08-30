from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50)


class Goods(models.Model):
    name = models.CharField(max_length=50)


class Client(models.Model):
    name = models.CharField(max_length=50)
    goods = models.ManyToManyField(Goods)
    city = models.ForeignKey(City)


class Supplier(models.Model):
    name = models.CharField(max_length=50)
    city = models.OneToOneField(City)
