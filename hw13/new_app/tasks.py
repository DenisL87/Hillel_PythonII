from __future__ import absolute_import, unicode_literals

from celery import shared_task
from bs4 import BeautifulSoup
import requests

from new_app.models import Quote, Author


@shared_task()
def parse(page, start, stop):
    URL = f'https://quotes.toscrape.com/page/{page}/'
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    quotes = soup.find_all("span", {"class": "text"})
    authors = soup.find_all("small", {"class": "author"})
    quotes.split("</span>, <span class='text' itemprop='text''>")
    authors.split("</small>, <small class='author' itemprop='author'>")

    authors_2_add = []
    quotes_2_add = []
    i = start
    while i <= stop:
        authors_2_add.append(Author(name=authors[i]))
        i += 1
    Author.objects.bulk_create(authors_2_add)

    author_ids = Author.objects.values_list('id', flat=True)
    i = start
    while i <= stop:
        quotes_2_add.append(Quote(text=quotes[i], author_id=author_ids[i]))
        i += 1
    Quote.objects.bulk_create(quotes_2_add)
