'''stringio_bytesio'''

# from io import StringIO

# # 初始化，说明指针指向0
# stringIO = StringIO("abc")
# print(stringIO.getvalue())
# print(stringIO.tell())

# # 写入字符d
# stringIO.write("d")
# print(stringIO.getvalue())
# print(stringIO.tell())

# # 移动指针到末尾
# stringIO.seek(0, 2)
# print(stringIO.getvalue())
# print(stringIO.tell())

# # 写入字符e
# stringIO.write("e")
# print(stringIO.getvalue())
# print(stringIO.tell())


# from io import StringIO
# f = StringIO()
# f.write('hello')
# f.write(' ')
# f.write('world!')
# print(f.getvalue())

# from io import StringIO
# f = StringIO('Hello!\nHi!\nGoodbye!')
# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s.strip())


# from io import BytesIO
# f = BytesIO()
# f.write('中文'.encode('utf-8'))
# print(f.getvalue())

# from io import BytesIO
# f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
# print(f.read())