from abc import abstractmethod


class Item:

    @abstractmethod
    def show(self):
        pass


class StandartHotDog_Item(Item):
    def __init__(self, data):
        self.name = data.name
        self.price = data.price

    def show(self):
        print(f'{self.name} - {self.price}')


class HandMade_HotDog_Item(Item):
    def __init__(self, data):
        self.name = data.name
        self.price = None
        self.ingredients = data.ingredients

    def show(self):
        st = f"{self.name} состоит из: "
        for i in self.ingredients:
            st += f'{i.name}, '

        return st


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

class Menu(Item):
    def show(self, *items):
        for item in items:
            item.show()