from abc import abstractmethod


# приветствие
# вывод общей информации о хот-догах стандартных и самодельном.
# вывод оплата картой
# вывод оплата наличными
# менюшка ??


class Item:

    @abstractmethod
    def show(self):
        pass


class StandartHotDogItem(Item):
    def __init__(self, data):
        self.name = data.name
        self.price = data.price

    def show(self):
        print(f'{self.name}. Стоимость - {self.price} рублей.')


class HandMadeHotDogItem(Item):
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


class ChosenHotDog:
    def get_chosen_hot_dog(self, choice, data):
        return data[choice - 1]


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


class ShowHotDogItems(Item):
    def show(self, *items):
        count = 0
        for item in items:
            count += 1
            print(f'{count} - ', end='')
            item.show()
