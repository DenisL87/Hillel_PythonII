from django.contrib import admin

from quickstart.models import User, Comment, Post

admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Post)
