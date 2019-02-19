'''lambda'''

lambda x: x * x
def f(x):
    return x * x
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
f = lambda x: x * x
print(f)
print(f(5))
def build(x, y):
    return lambda: x * x + y * y # x, y不用特意声明

def is_odd(n):
    return n % 2 == 1
L = list(filter(is_odd, range(1, 20)))
print(L)

L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(L)