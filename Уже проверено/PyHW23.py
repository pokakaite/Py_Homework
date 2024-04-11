# Задание 1
# К уже реализованному классу «Дробь» добавьте статический метод, который при вызове возвращает
# количество созданных объектов класса «Дробь».

class Sanrio:
    counter = 0
    def __init__(self, name):
        self.name = name
        Sanrio.counter += 1

    def show(self):
        print(f'{Sanrio.counter} - {self.name}')

    @staticmethod
    def count():
        print(f"Количество объектов класса Sanrio - {Sanrio.counter}")

HelloKitty = Sanrio("Hello Kitty")
Kuromi = Sanrio("Kuromi")
MyMelody = Sanrio("My melody")
HelloKitty.show()
Kuromi.show()
MyMelody.show()
Sanrio.count()
print()


# Задание 2
# Создайте класс для конвертирования температуры из
# Цельсия в Фаренгейт и наоборот. У класса должно быть
# два статических метода: для перевода из Цельсия в Фаренгейт и
# для перевода из Фаренгейта в Цельсий. Также
# класс должен считать количество подсчетов температурыи
# возвращать это значение с помощью статического метода.

class Temperature:
    counter = 0
    @staticmethod
    def toFahrenheit(celcium):
        Temperature.counter += 1
        print(f'{celcium} градусов по Цельсию это {(celcium * (9 / 5)) + 32} градусов по Фаренгейту')

    @staticmethod
    def toCelcium(fahrenheit):
        Temperature.counter += 1
        print(f'{fahrenheit} градусов по Фаренгейту это {(fahrenheit - 32) * (5 / 9)} градусов по Цельсию')

    @staticmethod
    def count():
        print(f'Количество подсчётов температуры - {Temperature.counter}')

Temperature.toCelcium(50)
Temperature.toCelcium(30)
Temperature.toFahrenheit(20)
Temperature.toFahrenheit(0)
Temperature.count()
print()

# Задание 3
# Создайте класс для перевода из метрической системы
# в английскую и наоборот. Функциональность необходимо
# реализовать в виде статических методов. Обязательно
# реализуйте перевод мер длины.

class Length:
    @staticmethod
    def toMile(metre):
        print(f"В {metre} метрах {metre / 1609.34} милей.")

    @staticmethod
    def toFoot(metre):
        print(f"В {metre} метрах {metre * 3.281} футов.")

    @staticmethod
    def toInch(metre):
        print(f"В {metre} метрах {metre * 39.37} дюймов.")

    @staticmethod
    def mileToMetre(mile):
        print(f"В {mile} милях {mile * 1609.34} метров.")

    @staticmethod
    def footToMetre(foot):
        print(f"В {foot} футах {foot / 3.281} метров.")

    @staticmethod
    def inchToMetre(inch):
        print(f"В {inch} дюймах {inch / 39.37} метров.")

Length.toMile(10)
Length.toFoot(10)
Length.toInch(10)
Length.mileToMetre(10)
Length.footToMetre(10)
Length.inchToMetre(10)