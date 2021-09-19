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
        Author.objects.bulk_create(authors)

        # Publishers creating
        publishers = []
        for i in range(10):
            publishers.append(Publisher(name='Publisher_' + str(i)))
        Publisher.objects.bulk_create(publishers)

        # Books creating
        books = []
        publisher_ids = Publisher.objects.values_list('id', flat=True)
        authors_ids = Author.objects.values_list('id', flat=True)
        for i in range(len(authors) * 50):
            # book_authors = []
            # authors_No = random.randint(1, 5)
            # authors_count = 0
            # while authors_count < authors_No:
            #     to_add = authors[random.randint(1, len(authors))]
            #     if to_add in book_authors:
            #         continue
            #     else:
            #         book_authors.append(to_add)
            #         authors_count += 1

            book_authors_ids = set([random.choice(authors_ids) for i in range(random.randint(1, 5))])
            book = Book(name='Book_' + str(i),
                        pages=random.randint(100, 1000),
                        price=random.uniform(10.0, 250.0),
                        rating=random.uniform(0.0, 5.0),
                        # authors_id=set([random.choice(authors_ids) for i in range(random.randint(1, 5))]),
                        publisher_id=random.choice(publisher_ids),
                        pubdate=datetime.date(2020, 2, 5)
                        )
            book.authors.add(*book_authors_ids)
            # book.author_set.add(authors[5], authors[6])
            # book.publisher_set.add(publishers[2])
            books.append(book)
        Book.objects.bulk_create(books)
