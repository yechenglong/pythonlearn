#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import functools
# def metric(fn):
#     @functools.wraps(fn)
#     def runtime(*args):
#         starttime=time.time()
#         func=fn(*args)
#         endtime=time.time()
#         print('%s executed in %s ms' % (fn.__name__, endtime-starttime))
#         return func
#     return runtime
# # 测试
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y;
#
# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z;
#
# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')

# 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
# def test(func):
#     @functools.wraps(func)
#     def write(*args):
#         print("%s begin call" % func.__name__)
#         fn=func(*args)
#         print("%s end call" % func.__name__)
#         return fn
#     return write
# # 测试
# @test
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y;
# @test
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z;
# f = fast(11, 22)
# s = slow(11, 22, 33)
# 再思考一下能否写出一个@log的decorator，使它既支持：
# @log
# def f():
#     pass
# 又支持：
# @log('execute')
# def f():
#     pass
def log(*a):
    if isinstance(a[0], str):
        text=a[0]
        def logxx(func):
            #@functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s %s():' % (text, func.__name__))
                return func(*args, **kw)
            return wrapper
        return logxx
    else:
        func=a[0]
                    #@functools.wraps(func)
        def wrapper(*args, **kw):
            print('call %s():' % func.__name__)
            return func(*args, **kw)
        return wrapper

@log('execute')
def f():
    pass
@log
def g():
    pass
f()
g()


