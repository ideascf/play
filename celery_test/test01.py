import time
import celery

app = celery.Celery('tasks', broker='redis://')

@app.task
def sendmail(mail):
    print('sending mail to %s...' % mail)
    time.sleep(2.0)
    print('mail sent.')
