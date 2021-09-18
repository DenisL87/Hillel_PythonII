import os

from datetime import timedelta

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hw13settings')

app = Celery('hw13')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {}

@app.task(bind=True)
def debug_task(self):
    print(f'Request {self.request!r}')
