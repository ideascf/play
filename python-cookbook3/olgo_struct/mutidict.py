# sample 1, keep the order
a = {
    'a': [1,2,3],
    'b': [4,5],
}

# sample 2, save distinctly
b = {
    'a': {1,2,3},
    'b': {2,2,3},
}

# sample 3, use defaultdict create multidict
# defaultdict, every not exist value is DEFAULT
from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(1)
d['b'].append(2)
print(d)

# sample 3.1
print()
d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(1)
d.setdefault('b', []).append(3)
print(d)