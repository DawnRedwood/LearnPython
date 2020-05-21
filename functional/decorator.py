'''decorator'''

# import functools
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
# @log
# def now():
#     print('2015-3-25')
# now()

# import functools
# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
# @log('execute')
# def now():
#     print('2015-3-25')
# now()

# import time, functools
# def metric(fn):
#     @functools.wraps(fn)
#     def wrapper(*args, **kw):
#         print('%s executed in %s ms' % (fn.__name__, 10.24))
#         return fn(*args, **kw)
#     return wrapper
# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y;
# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z;
# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')

# import functools
# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('Begin call')
#             if isinstance(text, str):
#                 print('%s %s():' % (text, func.__name__))
#             else:
#                 print('call %s():' % func.__name__) 
#             r = func(*args, **kw)
#             print('Eng call')
#             return r
#         return wrapper
#     return decorator if isinstance(text, str) else decorator(text)
# @log
# def f():
#     print('f is running.')
# f()
# @log('execute')
# def g():
#     print('g is running.')
# g()