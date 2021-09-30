from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from app.models import Book
from .forms import DeleteBookForm, CreateBookForm


class BooksListView(generic.ListView):
    model = Book
    queryset = Book.objects.prefetch_related('authors')
    paginate_by = 100

    template_name = 'catalog/books_list.html'


class CreateObjectView(LoginRequiredMixin, generic.CreateView):
    model = Book
    form = CreateBookForm()
    fields = ['name', 'authors', 'pages', 'price', 'publisher', 'rating', 'pubdate']
    template_name = 'catalog/create_object.html'

    def validate(request):
        if request.method == 'POST':
            form = CreateBookForm(request.POST)
            if form.is_valid():
                return HttpResponseRedirect('created')
        else:
            form = CreateBookForm()


class EditObjectView(LoginRequiredMixin, generic.UpdateView):
    model = Book
    fields = ['name', 'authors', 'price']

    template_name = 'catalog/edit_object.html'


class DeleteObjectView(LoginRequiredMixin, generic.DeleteView):
    model = Book
    form = DeleteBookForm()
    template_name = 'catalog/delete_object.html'
