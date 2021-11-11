from rest_framework.generics import ListAPIView

from .serializers import PersonSerializer
from ..models import Person


class PersonListAPIView(ListAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
