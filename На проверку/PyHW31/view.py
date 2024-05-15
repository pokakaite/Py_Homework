from hot_dog import *
from toppings import *


class MakeHotDog:
    def __init__(self):
        self.hot_dog = None

    def set_hot_dog(self):
        self.hot_dog = []

    def add_hot_dog(self, hot_dog):
        for i in hot_dog:
            self.hot_dog.append(i)

    def add_topping(self, topping):
        self.hot_dog.append(topping)

    def get_hot_dog(self):
        return self.hot_dog


class Menu():

    def greeting(self):
        print(f'\nДобро пожаловать в киоск. Я знаю, вы хотите попробовать наши знаменитые хот-доги.\n'
              f'Вы можете выбрать хот-дог из меню или создать свой.\n'
              f'Наши хот-доги:\n')

    def show_hot_dog_info(self, hot_dog):
        hot_dog.show_id()
        hot_dog.show_name()
        hot_dog.show_recipe()
        hot_dog.show_price()
        print()

    def from_menu_or_own(self):
        choice = int(input('''\nВыберите, что хотите сделать.
        1 - Выбрать хот-дог из меню,
        2 - Создать свой.\n'''))
        return choice

    def choose_hot_dog(self):
        choice = int(input(f'''\nКакой хот-дог хотите попробовать?
        1 - Стандартный,
        2 - Мексиканский,
        3 - Веганский
        '''))
        return choice

    def toppings_question(self):
        choice = int(input('''\nЖелаете добавить топпинги?
        1 - Да,
        2 - Нет
        '''))
        return choice

    def show_toppings(self, topping):
        print()
        topping.show_id()
        topping.show_name()
        topping.show_amount()

    def choose_topping(self):
        topping = int(input('\nВведите номер топпинга, который хотите добавить - '))
        return topping


menu = Menu()
menu.greeting()
menu.show_hot_dog_info(standart)
menu.show_hot_dog_info(mexican)
menu.show_hot_dog_info(vegan)
if menu.from_menu_or_own() == 1:
    menu.choose_hot_dog()
    menu.toppings_question()
    menu.show_toppings(show_onion)
    menu.show_toppings(show_jalapeno)
    menu.show_toppings(show_pickles)
    menu.show_toppings(show_cheese)
    menu.choose_topping()