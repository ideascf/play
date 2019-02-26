# coding=utf-8
import  time
import gc
import objgraph

class A(object):
    def __init__(self):
        self.fun = self.foo  # TAG1.  这一行代码将导致产生循环引用,
        pass

    def foo(self):
        pass

    def __del__(self):  # TAG2.  在python 3.4以后行为有变更: https://docs.python.org/3/library/gc.html#gc.garbage
        print 'deleted...'  # 注释掉TAG1，将会打印本行代码


a = A()
print len(gc.get_referents(a))  # 注释掉TAG1, 将打印1。 否则打印2
del a
gc.collect()

print gc.garbage  # 注释掉TAG2. 将会打印[], 否则打印[object-of-A]
print

print 'show most common types:'
objgraph.show_most_common_types()
