from celery import Celery
from celery import shared_task

# app = Celery('tasks', broker='pyamqp://guest@localhost//')
#
# @app.task
# def a_task():
#     pass