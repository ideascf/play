import heapq


class PriorityQueque:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # tuple is comparable, compare from 0 - n
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        *_, item = heapq.heappop(self._queue)
        return item

class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        # return 'Item({0})'.format(self.name)
        return 'Item({!r})'.format(self.name)



q = PriorityQueque()
q.push(Item([1,2,3, ('xx', 'yy')]), 5)
q.push(Item((3,2,1)), 4)
q.push(Item('hello'), 8)

print(q.pop())
print(q.pop())
print(q.pop())
# print(q.pop())
