from django.contrib import admin

from new_app.models import Quote, Author

admin.site.register(Author)
admin.site.register(Quote)
