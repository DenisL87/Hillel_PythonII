from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from .serializers import PersonSerializer
from ..models import Person


class PersonListAPIView(ListAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class NewEntryAPIView(CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class SearchAPIView(RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class EditAPIView(UpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class DeleteAPIView(DestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
