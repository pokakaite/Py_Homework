from model import *

class HotDog_Cache:

    cache = {}

    @staticmethod
    def load():
        chicken = Chicken()
        chicken.set_id("1")
        HotDog_Cache.cache[chicken.get_id()] = chicken

        pork = Pork()
        pork.set_id("2")
        HotDog_Cache.cache[pork.get_id()] = pork

        beef = Beef()
        beef.set_id("3")
        HotDog_Cache.cache[beef.get_id()] = beef

    @staticmethod
    def get_hot_dog(sid):
        hotdog = HotDog_Cache.cache.get(sid, None)
        return hotdog.clone()


def show():
    HotDog_Cache.load()

    chicken = HotDog_Cache.get_hot_dog("1")
    print(f'{chicken.get_id()} - {chicken.get_name()}')

    pork = HotDog_Cache.get_hot_dog("2")
    print(f'{pork.get_id()} - {pork.get_name()}')

    beef = HotDog_Cache.get_hot_dog("3")
    print(f'{beef.get_id()} - {beef.get_name()}')


def view():
    print(f'Добро пожаловать в наш киоск. Я знаю, вы хотите попробовать наши знаменитые хот-доги.\n'
          'Вот вам разные виды на выбор:\n')
    show()
    print()
    choice = input('Введите номер хот-дога, который хотите попробовать - ')
    print(HotDog_Cache.cache[choice].__repr__())

def add_smth():
    choice = input('''Введите название ингредиента, который хотите добавить - ''')
    ingredient = AddTopping(choice)
    print(ingredient.topping())

def add_smth_else():
    choice_adding = int(input('''\nХотите что-нибудь добавить?
        1 - Да
        2 - Нет
        '''))
    if choice_adding == 1:
        add_smth()
    else:
        pass

    return add_smth_else()


view()
add_smth_else()



