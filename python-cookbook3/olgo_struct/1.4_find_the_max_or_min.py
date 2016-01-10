# from set find the largest or smallest

import heapq

#### sample 1, compare by default value
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))  # [42, 37, 23]
print(heapq.nsmallest(3, nums))  # [-4, 1, 2]


#### sample 2, compare by assign key
print()
records = [
    {'name': 'xx', 'shares': 100, 'price': 9},
    {'name': 'yy', 'shares': 99, 'price': 8},
]
print(heapq.nlargest(1, records, key=lambda record: record['price']))  #    {'name': 'xx', 'shares': 100, 'price': 9},
print(heapq.nsmallest(1, records, key=lambda record: record['price']))  #    {'name': 'yy', 'shares': 99, 'price': 8},

#### sample 3, convert list into heapq
print()
l = [10, 8, -1, 1,2,3]
# hq = heapq.heapify(l) # DONT return anything
# 'Transform list into a heap, in-place, in O(len(heap)) time.'
heapq.heapify(l) # DO heap sort
print(type(l), l)


#### another
l  =[1,2,3]
m = max(l); print(m)  #  just for one
m = sorted(l)[-1]; print(m) # The wanted is closely l
m = heapq.nlargest(1, l)[0]; print(m) # get more but NOT closely l

# import utils; utils.dir_class(heapq)