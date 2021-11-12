from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response

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
    lookup_field = 'id'


class EditAPIView(UpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    http_method_names = ['get', 'head', 'post']

    def get(self, request, *args, **kwargs):
        serializer = PersonSerializer(Person.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        self.http_method_names.append("GET")
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteAPIView(DestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'id'
