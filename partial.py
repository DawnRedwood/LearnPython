'''partial'''

def int2(x, base=2):
    return int(x, base)
print(int2('1000000'))
print(int2('1010101'))

import functools
int2 = functools.partial(int, base=2)
print(int2('1000000'))
print(int2('1010101'))
print(int2('1000000', base=10))

int2 = functools.partial(int, base=2)
print(int2('10010'))
kw = { 'base': 2 }
print(int('10010', **kw))

max2 = functools.partial(max, 10)
print(max2(5, 6, 7))
args = (10, 5, 6, 7)
print(max(*args))