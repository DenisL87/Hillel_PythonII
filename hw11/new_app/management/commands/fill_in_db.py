import datetime

from django.core.management.base import BaseCommand
from faker import Faker
from faker.generator import random

from new_app.models import Author, Publisher, Book


class Command(BaseCommand):
    help = 'Filling out database'

    def handle(self, *args, **options):
        fake = Faker()
        authors = []
        # Authors creating
        for i in range(100):
            authors.append(Author(name=fake.name(), age=random.randint(30, 100)))
        Author.objects.bulk_create(authors, batch_size=len(authors), ignore_conflicts=False)

        # Publishers creating
        publishers = []
        for i in range(10):
            publishers.append(Publisher(name='Publisher_' + str(i)))
        Publisher.objects.bulk_create(publishers, batch_size=len(publishers), ignore_conflicts=False)

        # Books creating
        books = []
        for i in range(len(authors) * 50):
            book = Book(name='Book_' + str(i),
                        pages=random.randint(100, 1000),
                        price=random.uniform(10.0, 250.0),
                        rating=random.uniform(0.0, 5.0),
                        # authors=object.author_set.add(authors[4]),
                        # publisher=object.publisher_set.add(publishers[4]),
                        pubdate=datetime.date(2020, 2, 5)
                        )
            book.author_set.add(authors[5], authors[6])
            book.publisher_set.add(publishers[2])
            books.append(book)
        Book.objects.bulk_create(books, batch_size=len(books), ignore_conflicts=False)
