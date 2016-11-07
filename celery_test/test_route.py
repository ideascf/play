# coding=utf-8
import time
import celery
from kombu import Queue, Exchange

app = celery.Celery('tasks', broker='redis://')


"""
if queue is None and exchange is None:
    queue = self.default_queue
if queue is not None:
    if isinstance(queue, string_t):
        qname, queue = queue, self.queues[queue]
    else:
        qname = queue.name
    exchange = exchange or queue.exchange.name
    routing_key = routing_key or queue.routing_key
"""

exchange = Exchange('exchange_test', type='direct')
app.conf.update(
    CELERY_QUEUES=(
        Queue('queue_test', exchange=exchange, routing_key='abc'),
    ),
    CELERY_DEFAULT_EXCHANGE='exchange_c1',
    CELERY_DEFAULT_QUEUE='haha',
    CELERY_ROUTES={
        'hello': {
            # 如果配置了exchagne和routing_key会优先使用那两个参数.
            # 最后才是,从CELERY_QUEUES中的对应queue取exchange和routing_key
            # 相关代码见: celery/app/base.py:350, celery/app/ampq.py:230
            'queue': 'queue_c1',

            # 优先使用下面的两个参数,来路由task
            'exchange': 'exchange_test',
            'routing_key': 'abc',
        },
    },
)


@app.task
def sendmail(mail):
    print('sending mail to %s...' % mail)
    time.sleep(2.0)
    print('mail sent.')
