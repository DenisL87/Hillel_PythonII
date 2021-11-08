from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

from address_book.forms import AddressBookForm
from address_book.models import Person
from .forms import NewEntry


def address_book(request):
    data = Person.objects.all()
    return render(request, 'address_book.html', context={'People': data})


def new_entry(request):
    if request.method == 'POST':
        form = NewEntry(request.POST)
        if form.is_valid():
            person = Person(first_name=form.cleaned_data['first_name'],
                            last_name=form.cleaned_data['last_name'],
                            phone=form.cleaned_data['phone'],
                            address=form.cleaned_data['address'])
            person.save()
            return HttpResponseRedirect('address_book')
    else:
        form = NewEntry()
        return render(request, 'create_entry.html', {'form': form})


def delete_entry(request):
    pass


def edit_entry(request):
    pass


def search_entry(request):
    pass


# class CreateEntry(View):
#     def get(self, request):
#         form = AddressBookForm()
#         return render(request, 'create_entry.html', context={'form': form})
#
#     def post(self, request):
#         form = AddressBookForm(request.POST)
#         if form.is_valid():
#             new_entry = form.save()
#             return redirect(new_entry)
#         return render(request, 'create_entry.html', context={'form': form})
