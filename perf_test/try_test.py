import logging
import sys

from tools import decorator

def dumy(times=10000):
    a = 0
    for i in range(times):
        for j in range(10000):
            a += a

    return a

@decorator.timeit
def foo1():
    dumy()

@decorator.timeit
def foo2():
    try:
        dumy()
    except Exception as e:
        print(e)

@decorator.timeit
def foo3():
    for i in range(10000):
        try:
            dumy(1)
        except Exception as e:
            print(e)

@decorator.timeit
def foo4():
    for i in range(10000):
        dumy(1)

if __name__ == '__main__':
    foo1()
    foo2()
    foo3()
    foo4()
