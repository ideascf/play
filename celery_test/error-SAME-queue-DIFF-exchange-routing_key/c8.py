# coding=utf-8
import time
import celery
from kombu import Queue, Exchange


app = celery.Celery('tasks', broker='redis://')


exchange = Exchange('exchange_c8', type='direct')
app.conf.update(
    CELERY_QUEUES=(
        Queue('queue_same', exchange=exchange, routing_key='xyz'),
    ),
    CELERY_ROUTES={
        'hello': {
            'queue': 'queue_same',
        },
        'c8': {
            'queue': 'queue_same',
        }
    },
)


@app.task(name='hello')
def s(msg):
    print msg


@app.task(name='c8')
def c8():
    print 'c8'