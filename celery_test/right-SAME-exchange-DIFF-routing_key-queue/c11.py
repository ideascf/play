# coding=utf-8
import time
import celery
from kombu import Queue, Exchange


app = celery.Celery('tasks', broker='redis://')


exchange = Exchange('exchange_same', type='direct')
app.conf.update(
    CELERY_QUEUES=(
        Queue('queue_c11', exchange=exchange, routing_key='xyz'),
    ),
    CELERY_ROUTES={
        'hello': {
            'queue': 'queue_c11',
        },
    },
)


@app.task(name='hello')
def s(msg):
    print msg
