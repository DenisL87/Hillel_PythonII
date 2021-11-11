from rest_framework import serializers

from ..models import Person


class PersonSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    url = serializers.URLField(required=True)
    image = serializers.ImageField(required=True)

    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name', 'phone', 'address', 'url', 'image']
