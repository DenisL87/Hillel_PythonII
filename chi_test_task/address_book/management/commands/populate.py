from django.core.management.base import BaseCommand
from faker import Faker

from address_book.models import Person


class Command(BaseCommand):
    help = 'populate database'

    def handle(self, *args, **options):
        fake = Faker()
        people = []
        count = 0
        while count < 50:
            name = fake.name()
            name_arr = name.split(' ')
            people.append(Person(first_name=name_arr[0], last_name=name_arr[-1],
                                 phone=fake.phone_number(), address=fake.address()))
            count += 1
        Person.objects.bulk_create(people)
