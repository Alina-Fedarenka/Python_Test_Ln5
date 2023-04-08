# class Car:
#     name = "Q7"
#     make = "audi"
#     age = 2020
#
#     def start(self):
#         print('Start engine')
#
#     def stop(self):
#         print('Stop engine')
#
#
# car1 = Car()
# car2 = Car()
# # print(type(car1))
# # print(car1.age)
# # print(car1.name)
# # print(car1.make)
# # car1.start()
#
# print(car1.start())

# class Car:
#     age = 2020
#     name = 'Priora'
#     make = 'Lada'
#
#     def start(self, name, make = 'Audi'):
#         self.name = name
#         self.make = make
#         print(f"The {self.make} {self.name} 's engine is started")
#
#     def get_age(self):
#             print(f"Car {self.make} {self.name} {self.age} make")
#
# car3 = Car()
# print(car3.make)
# print(car3.start('Q7'))
# print(car3.get_age())

# class Cat:
#
#     name = 'Timmy'
#     def __init__(self):
#         print('Hello')


# class HockeyPlayer:
#     def __init__(self, first_name, last_name, goal = 0, assist = 0):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.goal = goal
#         self.assist = assist
#
#     def goals(self, goal):
#         self.goal = goal
#
#     def all_assist(self, assist=0):
#         self.assist = assist
#
#     def statistics(self):
#         print(f'Hockey player Name: {self.first_name} {self.last_name}')
#         print(f'Goals: {self.goal}')
#         print(f'Assist: {self.assist}')
#
# ovech = HockeyPlayer('Alexander', 'Ovechkin')
# ovech.goals(700)
# ovech.all_assist(500)
# ovech.statistics()
#
# vin = HockeyPlayer('Vincent', 'LeKavalier')
# vin.goals(500)
# vin.all_assist(600)
# vin.statistics()

# class Person(object):
#     def can_breathe(self):
#         print('I breathe')
#
#     def can_walk(self):
#         print('I walk')
#
#     def can_sleep(self):
#         print('I sleep')
#
# class Teacher(Person):
#     # def can_teach(self):
#     #     print('I teach')
#     #
#     # def can_breathe(self):
#     #     print('I breathe')
#     #
#     # def can_walk(self):
#     #     print('I walk')
#     #
#     # def can_sleep(self):
#     #     print('I sleep')
#     pass
#
# t1 = Teacher()
# t1.can_walk()
# t1.can_sleep()
# print(Teacher.__mro__)
# p1 = Person()
# p1.can_breathe()
# print(issubclass(Teacher, Person))
# print(issubclass(Person, object))
# print(issubclass(Teacher, object))


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        print(f'Кошке {self.name} {self.age} лет')

    def speak(self, sound):
        self.sound = sound
        print(f'Кошка сказала {self.sound}')

c1 = Cat('Дынька', 7)
c1.get_info()
c1.speak('Meow')























