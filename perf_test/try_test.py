from tools import perf


def dumy(times=10000):
    a = 0
    for i in range(times):
        for j in range(10000):
            a += a

    return a

@perf.timeit
def foo1():
    dumy()

@perf.timeit
def foo2():
    try:
        dumy()
    except Exception as e:
        print(e)

@perf.timeit
def foo3():
    for i in range(10000):
        try:
            dumy(1)
        except Exception as e:
            print(e)

@perf.timeit
def foo4():
    for i in range(10000):
        dumy(1)

if __name__ == '__main__':
    foo1()
    foo2()
    foo3()
    foo4()
