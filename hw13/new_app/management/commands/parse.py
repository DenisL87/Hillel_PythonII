from new_app import tasks

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Parsing'

    def handle(self, *args, **options):
        page = 1
        start = 0
        stop = 4
        while page < 11:
            while_count = 0
            while while_count < 2:
                tasks.parse.apply_async((page, start, stop), minute=0, second=0, hour="1-23/2")
                start += 5
                stop += 5
                while_count += 1
            page += 1
            start = 0
            stop = 4
