from gevent import monkey
monkey.patch_all()


import inspect
import threading
from gevent import threading as _threading
from gevent import event as _event

print inspect.getfile(threading.Event)
print inspect.getfile(threading.Condition)
print 'Lock', inspect.getfile(threading.Lock)
print 'RLock', inspect.getfile(threading.RLock)

print inspect.getfile(_event.Event)