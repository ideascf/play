# coding=utf-8
import time
import celery
from kombu import Queue, Exchange


app = celery.Celery('tasks', broker='redis://')


exchange = Exchange('exchange_c12', type='direct')
app.conf.update(
    CELERY_QUEUES=(
        Queue('queue_c12', exchange=exchange, routing_key='aaa'),
    ),
    CELERY_ROUTES={
        'hello': {
            'queue': 'queue_c12',
        },
    },
)


@app.task(name='hello')
def s(msg):
    print msg
