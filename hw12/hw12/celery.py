import os

from celery import Celery
# from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hw12.settings')

app = Celery('hw12')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
