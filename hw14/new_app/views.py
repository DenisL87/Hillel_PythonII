from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from new_app.models import Book


class BooksListView(generic.ListView):
    model = Book
    queryset = Book.objects.prefetch_related('authors')
    paginate_by = 10

    template_name = 'catalog/books_list.html'


class CreateObjectView(LoginRequiredMixin, generic.CreateView):
    model = Book
    fields = ['name', 'authors', 'price']

    template_name = 'catalog/create_object.html'


class EditObjectView(LoginRequiredMixin, generic.UpdateView):
    model = Book
    fields = ['name', 'authors', 'price']

    template_name = 'catalog/edit_object.html'


class DeleteObjectView(LoginRequiredMixin, generic.DeleteView):
    model = Book

    template_name = 'catalog/delete_object.html'
