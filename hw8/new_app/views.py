from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import PersonForm


def validate(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            new_person = form.save()
            return HttpResponseRedirect("/person/")
    if request.method == 'GET':
        form = PersonForm(request.GET)
        return render(request, 'person.html', {'form': form})


def poll_details(request, poll_id):
    obj = get_object_or_404(PersonForm, pk=poll_id)
    context = {'poll': obj}
    return render(request, 'poll_details.html', context)
