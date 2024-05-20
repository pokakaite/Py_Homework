from abc import abstractmethod


# вопросы приложения клиенту, вывод ответа

def make_dict(a=None, b=None, c=None, d=None, e=None):
    items = {
        1: a,
        2: b,
        3: c,
        4: d,
        5: e
    }
    return items

def choose_between(items, choice):
    try:
        return items.get(choice)()
    except:
        print('')


def choose_between_hot_dogs(items, choice):
    try:
        return items.get(choice)
    except:
        print('')


order_items = []
def add_to_order(item):
    order_items.append({item.name: item.price})


def add_topping(hot_dogs, hot_dog, ingredients, choice):
        hot_dogs[hot_dog - 1].add_ingredients(ingredients[choice - 1])
        hot_dogs[hot_dog - 1].show()


class Choice:
    def __init__(self):
        self.choice = None

    @abstractmethod
    def set_choice(self):
        pass

    @abstractmethod
    def get_choice(self):
        pass


class Greeting:

    def set_choice(self):
        print('''\nДобро пожаловать в киоск по продаже хот-догов.
        Вы можете выбрать из трёх стандартных хот-догов или создать свой.
        1 - Выбрать из стандартных.
        2 - Создать свой.''')
        self.choice = int(input('Ваш выбор - '))

    def get_choice(self):
        return self.choice


class ChooseHotDog:
    def set_choice(self):
        print('\nВведите номер хот-дога, который хотите попробовать.')
        self.choice = int(input('Ваш выбор - '))

    def get_choice(self):
        return self.choice


class AskForTopping:
    def set_choice(self):
        print('''\nЖелаете добавить топпинги?
        1 - Да
        2 - Нет''')
        self.choice = int(input('Ваш выбор - '))

    def get_choice(self):
        return self.choice


class ChooseTopping:
    def set_choice(self):
        self.choice = int(input('\nВведите номер топпинга, который хотите добавить - '))

    def get_choice(self):
        return self.choice


class ContinueToppings:
    def set_choice(self):
        print('''\nЖелаете продолжить добавлять топпинги?
        1 - Да
        2 - Нет''')
        self.choice = int(input('Ваш выбор - '))

    def get_choice(self):
        return self.choice


class ContinueHotDogs:
    def set_choice(self):
        print('''\nЖелаете заказать еще хот-дог?
        1 - Да
        2 - Нет''')
        self.choice = int(input('Ваш выбор - '))

    def get_choice(self):
        return self.choice
