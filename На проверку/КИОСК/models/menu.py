from abc import abstractmethod


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


class Order:
    def __init__(self):
        self.order_items = []

    def add_to_order(self, item):
        self.order_items.append({item.name: item.price})

    def show(self):
        print('\nВаш заказ:')
        count = 0
        for hot_dog in self.order_items:
            count += 1
            for name, price in hot_dog.items():
                print(f'{count} - {name} - {price} рублей.')
        if len(self.order_items) >= 3 and len(self.order_items) <= 5:
            print('Ваша скидка - 10%')
        elif len(self.order_items) >= 5 and len(self.order_items) <= 7:
            print('Ваша скидка - 15%')
        elif len(self.order_items) >= 7:
            print('Ваша скидка - 20%')


class Pay:
    def __init__(self):
        self.sum = []

    def add_to_sum(self, items):
        for hot_dog in items:
            for name, price in hot_dog.items():
                self.sum.append(price)

    def show(self, items):
        if len(items) >= 3 and len(items) <= 5:
            summ = sum(self.sum) - (sum(self.sum) * 0.1)
            print(f'\nСумма заказа - {summ} рублей.')
        elif len(items) >= 5 and len(items) <= 7:
            summ = sum(self.sum) - (sum(self.sum) * 0.15)
            print(f'\nСумма заказа - {summ} рублей.')
        elif len(items) >= 7:
            summ = sum(self.sum) - (sum(self.sum) * 0.2)
            print(f'\nСумма заказа - {summ} рублей.')
        else:
            summ = sum(self.sum)
            print(f'\nСумма заказа - {summ} рублей.')

class AddToFile:
    def add_to_file(self, order_items):
        with open('file.txt', 'w+', encoding='utf-8') as f:
            for hot_dog in order_items:
                for name, price in hot_dog.items():
                    f.write(f'{name} - {price} рублей.\n')


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


class ShowHotDogItems(Item):
    def __init__(self):
        self.items = []

    def get_items(self, *items):
        for item in items:
            self.items.append(item)

    def show(self):
        print()
        count = 0
        for item in self.items:
            count += 1
            print(f'{count} - ', end='')
            item.show()
