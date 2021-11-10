from django.test import TestCase

from address_book.models import Person


class PersonTestCase(TestCase):
    def setUp(self):
        Person.objects.create(first_name='John',
                              last_name='Johnson',
                              address='London',
                              phohe='124578',
                              url='')

