from gevent import monkey
monkey.patch_all()

import gevent
from gevent import hub
import traceback

def main():
    print('before')
    gevent.sleep(1)
    print('after')

def error_handler(*args, **kwargs):
    print(args, kwargs)

if __name__ == '__main__':
    try:
        g = gevent.spawn(main)

        # g.link(hub.get_hub().switch)
        hub.get_hub().switch()
        # gevent.joinall([g])
        # hub.get_hub().switch()
        # hub.get_hub().run()
        # hub.get_hub().loop.error_handler = error_handler
        # hub.get_hub().loop.run()
    except Exception as e:
        print('hello Exception')
        # print e
        traceback.print_exc()
