import celery
import time

app = celery.Celery('hello', broker='redis://localhost:36379/0')
app.conf.CELERY_RESULT_BACKEND = 'redis://localhost:36379/0'

@app.task
def hello(info):
    return 'world'

@app.task
def sleep(second=5):
    time.sleep(second)

    return second
