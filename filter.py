'''filter'''

# def is_odd(n):
#     return n % 2 == 1
# print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
# def not_empty(s):
#     return s and s.strip()
# print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

# def _odd_iter():
#     n = 3
#     while True:
#         yield n
#         n = n + 2
# def _not_divisible(n):
#     return lambda x: x % n != 0 # 返回的是lambda函数而不是值
# def primes():
#     yield 2
#     it = _odd_iter()
#     while True:
#         n = next(it)
#         yield n
#         it = filter(_not_divisible(n), it) 起筛选作用的是lambda函数而不是_not_divisible函数，所以带参数
# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break

# def is_palindrome(n):
#     num = str(n)
#     return num == num[::-1]

# # 测试:
# output = filter(is_palindrome, range(1, 1000))
# print('1~1000:', list(output))
# if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
#     print('测试成功!')
# else:
#     print('测试失败!')