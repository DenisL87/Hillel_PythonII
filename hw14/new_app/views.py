from django.shortcuts import render
from django.views import generic

from new_app.models import Book


class BooksList(generic.ListView):
    model = Book
    queryset = Book.objects.prefetch_related('authors')
    # queryset = Book.objects.all()
    paginate_by = 10

    template_name = 'catalog/books_list.html'
