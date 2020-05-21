'''regex'''

import re

# print(re.match(r'^\d{3}-\d{3,8}$', '010-12345'))
# print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))
# test = '010 12345'
# if re.match(r'^\d{3}\-\d{3,8}$', test):
#     print('ok')
# else:
#     print('failed')

# print('a b   c'.split(' '))
# print(re.split(r'\s+', 'a b   c'))
# print(re.split(r'[\s\,]+', 'a,b, c  d'))
# print(re.split(r'[\s\,\;]+', 'a,b;; c  d'))

# m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
# print(m)
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))

# t = '19:05:30'
# m = re.match(r'^([0-1][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$', t)
# print(m)
# print(m.groups())

# print(re.match(r'^(\d+)(0*)$', '102300').groups())
# print(re.match(r'^(\d+?)(0*)$', '102300').groups())

# re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# for i in range(100):
#     print(re_telephone.match('010-12345').groups())

# for i in range(100):
#     print(re.match(r'^(\d{3})-(\d{3,8})$', '010-12345').groups())


# import re

# def is_valid_email(addr):
#     if re.match(r'^[\w.]+@\w+\.com$', addr):
#         return True

# # 测试:
# assert is_valid_email('someone@gmail.com')
# assert is_valid_email('bill.gates@microsoft.com')
# assert not is_valid_email('bob#example.com')
# assert not is_valid_email('mr-bob@example.com')
# print('ok')


# import re

# def name_of_email(addr):
#     g = re.match(r'^(<([A-Z][a-z]+\s[A-Z][a-z]+)>\s)?([\w.]+)@\w+\.(org|com)$', addr)
#     if g.group(2):
#         return g.group(2)
#     else:
#         return g.group(3)

# # 测试:
# assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
# assert name_of_email('tom@voyager.org') == 'tom'
# print('ok')