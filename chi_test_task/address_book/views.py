from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from address_book.models import Person
from .forms import NewEntry, SearchEntry, EditEntry, DeleteEntry, AddressBookForm


def address_book(request):
    data = Person.objects.all()
    return render(request, 'address_book.html', context={'people': data})


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


def search_entry(request):
    if request.method == 'POST':
        form = SearchEntry(request.POST)
        if form.is_valid():
            input = form.cleaned_data['input']
            form.matches.append(Person.objects.filter(input))
        return render(request, 'search_entry.html', {'form': form})
    else:
        form = SearchEntry()
        return render(request, 'search_entry.html', {'form': form})


def edit_entry(request, index):
    if request.method == 'POST':
        form = EditEntry(request.POST)
        if form.is_valid():
            Person.objects.filter(id=index).update(first_name=form.cleaned_data['first_name'],
                                                   last_name=form.cleaned_data['last_name'],
                                                   phone=form.cleaned_data['phone'],
                                                   address=form.cleaned_data['address'])
        # person.save()
        return HttpResponseRedirect('address_book')


def delete_entry(request, index):
    person = get_object_or_404(Person, id=index)
    if request.method == 'POST':
        person.delete()
        return HttpResponseRedirect('address_book')
