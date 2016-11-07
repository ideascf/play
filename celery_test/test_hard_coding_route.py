# coding=utf-8
import time
import celery

app = celery.Celery('tasks', broker='redis://')

"""
1. 创建 `_kombu.binding.hard-coding_queue` 的exchange
2. 路由信息为: `1) "hard-coding_queue\x06\x16\x06\x16hard-coding_queue"`
3. **不推荐**使用硬编码task的路由
"""

@app.task(queue='hard-coding_queue')
def sendmail(mail):
    print('sending mail to %s...' % mail)

