# 5.1. Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов;
# как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания значений этого атрибута
# нужно использовать методы get и set
# 5.2. Cоздайте репозиторий на Github и отправте файл с домашним заданием в этот удаленный репозиторий
#import self as self


class Country:
    continent_class = 'North America'
    def __init__(self, name, capital_city, language, population):
        self.__name = name
        self.capital_city = capital_city
        self.language = language
        self.population = population

    def show_capital_city(self):
        return self.capital_city

    def get_name(self):
        return f'The country is {self.__name}.'

    def set_name(self, new_name):
        self.__name = new_name

    def show_population(self):
        return f'{self.__name} population is {self.population}'


country1 = Country('USA', 'Washington DC', 'English', 331.9)

# print(country1.name)
# country1.name = 'United States of America'
# print(country1.get_name())
print(country1.set_name('United States of America'))
# print(country1.get_name())
print(country1.__dict__)
print(country1._Country__name)
# print(country1.__dict__)
# print(country1.name)
# print(country1.get_name())
# print(country1.show_capital_city())
# print(country1.show_population())
# print(country1.continent_class())

# country2 = Country('Canada', 'Ottawa', 'English, French', 39.566)
# print(country2.name)
# print(country2.get_name())
# print(country2.show_capital_city())
# print(country2.show_population())
# print(country2.continent_class())

# class Mexico(Country):
#
#     def__init__(self, name, capital_city, language, population, phone_code):
#         super().__init__(name, capital_city, language, population)
#         self.phone_code = code
#
#
#     def nice_weather(self):
#         return "It's always nice outside!"
#
#
# country3 = Mexico('Mexico','Mexico City', 'Spanish', 129.150 )
# print(country3.__init__())
# print(country3.show_capital_city())

