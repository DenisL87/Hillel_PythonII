from django.contrib import admin

from app.models import Author, Store, Book, Publisher

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Store)
