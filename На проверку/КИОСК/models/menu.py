from abc import abstractmethod


class Greeting:
    def __init__(self):
        self.choice = None

    def greeting(self):
        print('''Добро пожаловать в киоск по продаже хот-догов.
        Вы можете выбрать из трёх стандартных хот-догов или создать свой.
        1 - Выбрать из стандартных.
        2 - Создать свой.''')
        self.choice = int(input('Ваш выбор - '))

    def get_choice(self):
        return self.choice


class Item:

    @abstractmethod
    def show(self):
        pass


class StandartHotDog_Item(Item):
    def __init__(self, data):
        self.name = data.name
        self.price = data.price

    def show(self):
        print(f'{self.name}. Стоимость - {self.price} рублей.')


class HandMade_HotDog_Item(Item):
    def __init__(self, data):
        self.name = data.name
        self.price = data.price
        self.ingredients = data.ingredients

    def show(self):
        st = f"{self.name} состоит из: "
        for i in self.ingredients:
            st += f'{i.name}, '
        st = st[:-2]
        st += '. '
        st += f"Стоимость - {self.price} рублей."
        print(st)


class CashPayItem(Item):
    def __init__(self, price):
        self.price = price

    def show(self):
        print(f'Вы оплатили наличными - {self.price}')


class CardPayItem(Item):

    def __init__(self, price):
        self.price = price

    def show(self):
        print(f'Вы оплатили картой - {self.price}')


class PayShowItem(Item):
    def show(self):
        print(f'Способ оплаты:')


class PayItem(Item):
    def show(self):
        return


class Menu(Greeting, Item):
    def show(self, *items):
        count = 0
        for item in items:
            count += 1
            print(f'{count} - ', end='')
            item.show()