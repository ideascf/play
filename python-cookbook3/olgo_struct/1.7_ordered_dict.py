import json
from collections import OrderedDict
import collections

def orderd_dict():
    d = OrderedDict() #     'Dictionary that remembers insertion order'
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4

    for key in d:
        print(key, d[key])

    print(json.dumps(d))


def unordered_dict():
    d = dict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4

    for key in d:
        print(key, d[key])

    print(json.dumps(d))

if __name__ == '__main__':
    orderd_dict()
    print()
    unordered_dict()