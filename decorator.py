# -*- coding:utf-8 -*-
"""
装饰器本质是一个函数，它可以在不改变原来的函数的基础上额外的增加一些功能，
返回值也是函数
"""

#********************************
#函数装饰器
def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == 'warn':
               print("%s is running" % func.__name__)
            return func(*args)
        return wrapper
    return decorator

@use_logging(level='warn')
def foo(name='foo'):
    print("i am %s" % name)

foo()

#******************************
#类装饰器
class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print("begin")
        self._func()
        print("end")

@Foo
def bar():
    print('bar')

bar()

#***********************************
def Before(request, kargs):
    print('before')

def After(request, kargs):
    print('after')

def Filter(before_func, after_func):
    def outer(main_func):
        def wrapper(request,kargs):
            before_result = before_func(request,kargs)
            if before_result != None:
                return before_result
            main_result = main_func(request, kargs)  #Index
            if main_result != None:
                return main_result
            after_result = after_func(request, kargs)
            if after_result != None:
                return after_result
        return wrapper
    return outer

@Filter(Before, After)  #参数为两个函数
def Index(request, kargs):
    print('index')

Index('ok', 'no')

#***********************************
def decorate(func):
    def wrapper(*args, **kwargs):
        print("begin")
        func(*args, **kwargs)
    return wrapper
@decorate
def text1():
    print("text1")

text1()

#带参数的装饰器,带参数的装饰器与普通的装饰器多加了一层
def func_name(name):
    def decorate(func):
        def wrapper(*args, **kwargs):
            print("begin with %s" % name)
            func(*args, **kwargs)
        return wrapper
    return decorate
@func_name("Ming")
def text1():
    print("text1")

text1()


