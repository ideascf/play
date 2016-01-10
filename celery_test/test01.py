import time
import celery

cel = celery.Celery('tasks', broker='redis://')

@cel.task
def sendmail(mail):
    print('sending mail to %s...' % mail)
    time.sleep(2.0)
    print('mail sent.')
