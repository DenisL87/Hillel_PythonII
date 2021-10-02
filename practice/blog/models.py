from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    text = models.TextField()
    author = models.ManyToManyField(User)
    is_published = models.BooleanField(default=False)


class Comment(models.Model):
    text = models.TextField()
    is_published = models.BooleanField(default=False)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
