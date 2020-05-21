'''os'''

# import os
# print(os.name)
# print(os.environ)
# print(os.environ.get('PATH'))
# print(os.environ.get('x', 'default'))

# print(os.path.abspath('.'))
# print(os.path.join('\\Users\\Dawn', 'testdir'))
# os.mkdir('\\Users\\Dawn\\testdir') # 默认是C盘
# os.rmdir('\\Users\\Dawn\\testdir')
# print(os.path.split('\\Users\\Dawn\\Desktop\\test.py'))
# os.rename('1.txt', '1.py')
# os.remove('1.py')

# print([x for x in os.listdir('.') if os.path.isdir(x)])
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])


# from datetime import datetime
# import os

# path = os.path.abspath('.')

# print('Name                          LastModified       Size')
# print('-----------------------------------------------------')

# for f in os.listdir(path):
#     flag = '/' if os.path.isdir(f) else ''
#     f += flag
#     time = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
#     size = os.path.getsize(f)
#     print(f.ljust(30) + time + '   ' + str(size))


# import os

# def find_str(string='', directory='.'):
#     for n in os.listdir(directory):
#         name = os.path.join(directory, n)
#         if os.path.isdir(name):
#             find_str(string, name)
#         elif string in name:
#             print(name)

# s = input('Please input the string that need to find: ')
# find_str(s)