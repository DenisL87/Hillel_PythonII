from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)


class Quote(models.Model):
    text = models.CharField(max_length=500)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
