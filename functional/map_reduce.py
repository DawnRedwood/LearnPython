'''map'''

# def f(x):
#     return x * x
# r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(list(r))
# print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

# def normalize(name):    
#     return name[0].upper() + name[1:].lower()

# # 测试:
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)


'''reduce'''

# from functools import reduce
# def add(x, y):
#     return x + y
# print(reduce(add, [1, 3, 5, 7, 9]))
# def fn(x, y):
#     return x * 10 + y
# print(reduce(fn, [1, 3, 5, 7, 9]))
# def char2num(s):
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, 
#         '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     return digits[s]
#     # return int(s)
# reduce(fn, map(char2num, '13579'))
# DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, 
#     '6': 6, '7': 7, '8': 8, '9': 9}
# def str2int(s):
#     def fn(x, y):
#         return x * 10 +y
#     def char2num(s):
#         return DIGITS[s]
#     return reduce(fn, map(char2num, s))
# def str2int(s):
#     def char2num(s):
#         return DIGITS[s]
#     return reduce(lambda x, y: x * 10 + y, map(char2num, s))

# from functools import reduce
# def prod(L):
#     return reduce(lambda x, y: x * y, L)

# # 测试:
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')

# from functools import reduce
# def str2float(s):
#     # return reduce(lambda x, y: x * 10 + y, map(int, s))
#     for i in range(len(s)):
#         if s[i] == '.':
#             count = i
#             break
#     f1 = reduce(lambda x, y: x * 10 + y, map(int, s[:count]))
#     f2 = reduce(lambda x, y: x * 0.1 + y, map(int, s[-1:count:-1]))
#     return f1 + 0.1 * f2

# from functools import reduce
# def str2float(s):
#     m = len(s) - s.index('.') - 1
#     def char2num(s):
#         digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,'9':9, '.':None}
#         return digits[s]
#     def fn(x, y):
#         if y == None:
#             return x
#         else:
#             return x * 10 + y
#     return reduce(fn, map(char2num, s), 0)/(10 ** m)

# # 测试:
# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')

# from functools import reduce
# CHAR_TO_FLOAT = {
#     '0': 0,
#     '1': 1,
#     '2': 2,
#     '3': 3,
#     '4': 4,
#     '5': 5,
#     '6': 6,
#     '7': 7,
#     '8': 8,
#     '9': 9,
#     '.': -1
# }
# def str2float(s):
#     nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
#     point = 0
#     def to_float(f, n):
#         nonlocal point
#         if n == -1:
#             point = 1
#             return f
#         if point == 0:
#             return f * 10 + n
#         else:
#             point = point * 10
#             return f + n / point
#     return reduce(to_float, nums, 0)

# print(str2float('0'))
# print(str2float('123.456'))
# print(str2float('123.45600'))
# print(str2float('0.1234'))
# print(str2float('.1234'))
# print(str2float('120.0034'))