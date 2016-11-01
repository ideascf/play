# coding=utf-8
import time
import celery
from kombu import Queue, Exchange


app = celery.Celery('tasks', broker='redis://')
app.conf.update(
    CELERY_DEFAULT_QUEUE='queue_c4'
)


@app.task(name='hello')
def s(msg):
    print msg
