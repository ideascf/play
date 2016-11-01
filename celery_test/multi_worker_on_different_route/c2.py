# coding=utf-8
import time
import celery
from kombu import Queue, Exchange


app = celery.Celery('tasks', broker='redis://')


exchange = Exchange('exchange_c2', type='direct')
app.conf.update(
    CELERY_QUEUES=(
        Queue('queue_c2', exchange=exchange, routing_key='xyz'),
        Queue('queue_c1', exchange=exchange, routing_key='abc'),
    ),
    CELERY_DEFAULT_EXCHANGE='exchange_c2',
    CELERY_DEFAULT_QUEUE='queue_c2',
    CELERY_ROUTES={
        'hello': {
            'queue': 'queue_c2',
        },
    },
    CELERY_CREATE_MISSING_QUEUES=False,
)


@app.task(name='hello')
def s(msg):
    print msg
