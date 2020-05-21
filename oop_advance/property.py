'''property'''

# class Student(object):
#     def get_score(self):
#         return self._score
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
# s = Student()
# s.set_score(60)
# print(s.get_score())
# # s.set_score(9999)
# # s.set_score('abc')

# class Student(object):
#     @property
#     def score(self):
#         return self._score
#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
# s = Student()
# s.score = 60
# print(s.score)
# # s.score = 9999

# class Student(object):
#     @property
#     def birth(self):
#         return self._birth
#     @birth.setter
#     def birth(self, value):
#         self._birth = value
#     @property
#     def age(self):
#         return 2015 - self._birth
# s = Student()
# s.birth = 12
# # s.age = 12

# class Screen(object):
#     @property
#     def width(self):
#         return self._width
#     @width.setter
#     def width(self, width):
#         if not isinstance(width, (int, float)):
#             raise ValueError('width must be valid!')
#         if width <= 0:
#             raise ValueError('width must be positive!')
#         self._width = width
#     @property
#     def height(self):
#         return self._height
#     @height.setter
#     def height(self, height):
#         if not isinstance(height, (int, float)):
#             raise ValueError('height must be valid!')
#         if height <= 0:
#             raise ValueError('height must be positive!')
#         self._height = height
#     @property
#     def resolution(self):
#         return self._width * self._height

# # 测试:
# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution =', s.resolution)
# if s.resolution == 786432:
#     print('测试通过!')
# else:
#     print('测试失败!')
