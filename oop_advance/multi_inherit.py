'''multi_inherit'''

# class Animal(object):
#     pass
# # 大类
# class Mammal(Animal):
#     pass
# class Bird(Animal):
#     pass
# # 其他类
# class Runnable(object):
#     def run(self):
#         print('Running...')
# class Flyable(object):
#     def fly(self):
#         print('Flying...')
# # 各种动物
# class Dog(Mammal, Runnable):
#     pass
# class Bat(Mammal, Runnable):
#     pass
# class Parrot(Bird, Flyable):
#     pass
# class Ostrich(Bird, Flyable):
#     pass

# class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
#     pass
# class MyTCPServer(TCPServer, ForkingMixIn):
#     pass
# class MyUDPServer(UDPServer, ThreadingMixIn):
#     pass
# class MyTCPServer(TCPServer, CoroutineMixIn):
#     pass