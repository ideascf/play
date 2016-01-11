import celery

app = celery.Celery('hello', broker='redis://localhost:36379/0')
app.conf.CELERY_RESULT_BACKEND = 'redis://localhost:36379/0'

@app.task
def hello(info):
    print info

    return 'world'
