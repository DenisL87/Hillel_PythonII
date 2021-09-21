from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hw13.settings')

app = Celery('hw13')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'parse': {
#         'task': 'tasks.parse',
#         'schedule': crontab(minute=0, second=0, hour="1-23/2"),
#         'args':
#     }
# }

