'''切片'''

# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# print([L[0], L[1], L[2]])
# r = []
# for i in range(3):
#     r.append(L[i])
# print(r)
# print(L[0:3])
# print(L[:3])
# print(L[1:3])
# print(L[-2:])
# L = list(range(100))
# print(L[:10])
# print(L[-10:])
# print(L[10:20])
# print(L[:10:2])
# print(L[::5])
# print(L[:])
# T = (0, 1, 2, 3, 4, 5)
# print(T[:3])
# S = 'ABCDEFG'
# print(S[:3])
# print(S[::2])

# def trim(s):
#     if s == '':
#         return s
#     elif s[0] == ' ':
#         s = s[1:]
#         return trim(s)
#     elif s[-1] == ' ':
#         s = s[:-1]
#         return trim(s)
#     return s
# # 测试:
# if trim('hello  ') != 'hello':
#     print('测试失败1!')
# elif trim('  hello') != 'hello':
#     print('测试失败2!')
# elif trim('  hello  ') != 'hello':
#     print('测试失败3!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('测试失败4!')
# elif trim('') != '':
#     print('测试失败5!')
# elif trim('    ') != '':
#     print('测试失败6!')
# else:
#     print('测试成功7!')


'''迭代'''

# d = {'a': 1, 'b': 2, 'c': 3}
# for key in d:
#     print(key)
# for value in d.values():
#     print(value)
# for k, v in d.items():
#     print(k, v)
# for ch in 'ABC':
#     print(ch)
# from collections.abc import Iterable
# print(isinstance('abc', Iterable))
# print(isinstance([1, 2, 3], Iterable))
# print(isinstance(123, Iterable))
# for i, value in enumerate(['A', 'B', 'C']):
#     print(i, value)
# for x, y in [(1, 1), (2, 4), (3, 9)]:
#     print(x, y)

# def findMinAndMax(L):
#     if L == []:
#         return (None, None)
#     min = L[0]
#     max = L[0]
#     for i in L:
#         if i < min:
#             min = i
#         if i > max:
#             max = i
#     return (min, max)

# # 测试:
# if findMinAndMax([]) != (None, None):
#     print('测试失败!')
# elif findMinAndMax([7]) != (7, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print('测试失败!')
# else:
#     print('测试成功!')


'''列表生成式'''
# print(list(range(1, 11)))
# L = []
# for x in range(1, 11):
#     L.append(x * x)
# print(L)
# print([x * x for x in range(1, 11)])
# print([x * x for x in range(1, 11) if x % 2 == 0])
# print([m + n for m in 'ABC' for n in 'XYZ'])
# import os
# print([d for d in os.listdir('.')])
# d = {'x': 'A', 'y': 'B', 'z': 'C'}
# print([k + '=' + v for k, v in d.items()])
# L = ['Hello', 'World', 'IBM', 'Apple']
# print([s.lower() for s in L])

# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [s.lower() for s in L1 if isinstance(s, str)]
# L3 = [s.lower() if isinstance(s,str) else s for s in L1] 

# # 测试:
# print(L2)
# print(L3)
# if L2 == ['hello', 'world', 'apple']:
#     print('测试通过!')
# else:
#     print('测试失败!')


'''生成器'''

# L = [x * x for x in range(10)]
# print(L)
# g = (x * x for x in range(2))
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# g = (x * x for x in range(10))
# for n in g:
#     print(n)
# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield(3)
#     print('step 3')
#     yield 5
# o = odd()
# print(next(o))
# print(next(o))
# print(next(o))
# print(next(o))
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
# # a, b = b, a + b
# # t = (b, a + b)
# # a = t[0]
# # b = t[1]
# print(fib(6))
# for n in fib(6):
#     print(n)
# g = fib(6)
# while True:
#     try:
#         x = next(g)
#         print('g:', x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break

# def triangles():
#     L = [1]
#     while True:
#         yield L
#         L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]

# n = 0
# results = []
# for t in triangles():
#     print(t)
#     results.append(t)
#     n = n + 1
#     if n == 10:
#         break
# if results == [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#     [1, 5, 10, 10, 5, 1],
#     [1, 6, 15, 20, 15, 6, 1],
#     [1, 7, 21, 35, 35, 21, 7, 1],
#     [1, 8, 28, 56, 70, 56, 28, 8, 1],
#     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# ]:
#     print('测试通过!')
# else:
#     print('测试失败!')

# def triangles():
#     L = [1]
#     while True:
#         yield L
#         L = [L[0] + 2] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [L[0] + 2]
# n = 0
# results = []
# for t in triangles():
#     print(t)
#     results.append(t)
#     n = n + 1
#     if n == 10:
#         break


'''迭代器'''

# from collections.abc import Iterable
# print(isinstance([], Iterable))
# print(isinstance({}, Iterable))
# print(isinstance('abc', Iterable))
# print(isinstance((x for x in range(10)), Iterable))
# print(isinstance(100, Iterable))
# from collections.abc import Iterator
# print(isinstance((x for x in range(10)), Iterator))
# print(isinstance([], Iterator))
# print(isinstance({}, Iterator))
# print(isinstance('abc', Iterator))
# print(isinstance(iter([]), Iterator))
# print(isinstance(iter('abc'), Iterator))
