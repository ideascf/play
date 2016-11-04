import time
import celery
from celery.exceptions import Retry, MaxRetriesExceededError

app = celery.Celery('tasks', broker='redis://')

@app.task(name='sendmail', bind=True, max_retries=2, default_retry_delay=1)
def sendmail(self, mail):
    try:
        self.retry()
    except Retry as e:
        print '#####retry', e
        raise
    except MaxRetriesExceededError as e:
        print '####max retries.', e
        raise
