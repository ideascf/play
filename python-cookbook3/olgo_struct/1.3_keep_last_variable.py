# sometime, may you want keep the limit history. yeah, for example: just last five.

# append and pop, from RIGHT direction
# 在队列两端插入或删除元素时间复杂度都是O(1)，而在列表的开头插入或删除元素的时间复杂度为O(N)。
from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history) # create deque, save almostly five values.
    for line in lines:
        if pattern in lines:
            yield line, previous_lines

        previous_lines.append(line)





##### another sample
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)

print(q) # 3,4,5

###### sample use deque
q = deque()
q.append(1)  # 1
q.append(2)  # 1,2
q.appendleft(3)  # 3,1,2
q.pop() # 3,1
q.popleft()  # 1
print(q)

for v in q:
    print(v)

list(
    map(
        lambda n: print(n),
        filter(
            lambda name: not name.startswith('__'),
            dir(q)
        )
    )
)
#
# for method in dir(q):
#     print(method)