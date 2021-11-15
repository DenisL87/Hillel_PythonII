from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView,
                                     CreateAPIView,
                                     UpdateAPIView,
                                     DestroyAPIView)
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import PersonSerializer
from ..models import Person


class DeleteAPIView(RetrieveAPIView, DestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'id'


class EditAPIView(RetrieveAPIView, UpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class NewEntryAPIView(CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonListAPIView(ListAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ['id', 'first_name', 'last_name', 'phone', 'address', 'url']
    filter_fields = ['id', 'first_name', 'last_name', 'phone', 'address', 'url']
