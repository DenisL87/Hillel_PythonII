from django.contrib import admin

from new_app.models import Author, Book, Publisher, Store

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Store)
