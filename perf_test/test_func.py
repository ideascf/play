# coding=utf-8

"""
测试函数调用的开销。

对比使用函数取获得字典中的key/value,和直接获取字典中的key/value的QPS。
"""
from perf import decorator
import perf

perf.set_profile_log()

d = {1:2}

@decorator.qps(duration_second=10)
def run_without_func():
    return d[1]


def get_func(key, data):
    return data[key]

@decorator.qps(duration_second=10)
def run_with_func():
    return get_func(1, d)


run_with_func()
run_without_func()
