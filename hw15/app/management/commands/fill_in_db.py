import random
from datetime import datetime

from django.core.management.base import BaseCommand
from faker import Faker

from app.models import Author, Publisher, Book, Store


class Command(BaseCommand):
    help = 'Filling in database'

    def handle(self, *args, **options):
        fake = Faker()
        authors = []
        for i in range(30):
            authors.append(Author(name=fake.name(), age=random.randint(30, 100)))
        Author.objects.bulk_create(authors)

        publishers = []
        for i in range(5):
            publishers.append(Publisher(name=fake.name()))
        Publisher.objects.bulk_create(publishers)

        publisher_ids = Publisher.objects.values_list('id', flat=True)
        authors_ids = Author.objects.values_list('id', flat=True)
        books = []
        for i in range(100):
            books.append(Book(name='book_' + str(i),
                              pages=random.randint(50, 1000),
                              price=random.uniform(5.0, 500.0),
                              rating=random.uniform(0.0, 5.0),
                              publisher_id=random.choice(publisher_ids),
                              pubdate=datetime.now()))
        Book.objects.bulk_create(books)
        books_qs = Book.objects.all()
        for book in books_qs:
            book_auth_ids = set([random.choice(authors_ids) for i in range(random.randint(1, 4))])
            book.authors.add(*book_auth_ids)
