# coding=utf-8
import time
import celery
from kombu import Queue, Exchange


app = celery.Celery('tasks', broker='redis://')


exchange = Exchange('exchange_c1', type='direct')
app.conf.update(
    CELERY_QUEUES=(
        Queue('queue_c1', exchange=exchange, routing_key='abc'),
        Queue('queue_test',)
    ),
    CELERY_DEFAULT_EXCHANGE='exchange_c1',
    CELERY_DEFAULT_QUEUE='haha',
    CELERY_ROUTES={
        'hello': {
            'queue': 'queue_c1',
        },
    },
)


@app.task(name='hello')
def s(msg):
    print msg
