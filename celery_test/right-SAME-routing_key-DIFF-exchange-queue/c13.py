# coding=utf-8
import time
import celery
from kombu import Queue, Exchange


app = celery.Celery('tasks', broker='redis://')


exchange = Exchange('exchange_c13', type='direct')
app.conf.update(
    CELERY_QUEUES=(
        Queue('queue_c13', exchange=exchange, routing_key='aaa'),
    ),
    CELERY_ROUTES={
        'hello': {
            'queue': 'queue_c13',
        },
    },
)


@app.task(name='hello')
def s(msg):
    print msg
