from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50, required=True)
    email = models.EmailField(required=True)
    password = models.CharField(max_length=50, required=True)


class Comment(models.Model):
    author = models.ForeignKey(User)


class Post(models.Model):
    title = models.CharField(max_length=50, required=True)
    author = models.ForeignKey(User)